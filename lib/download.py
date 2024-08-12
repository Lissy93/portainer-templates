import os
import csv
import requests
import json

dir = os.path.dirname(os.path.abspath(__file__))

destination_dir = os.path.join(dir, '../sources')
sources_list = os.path.join(dir, '../sources.csv')

# Downloads the file from a given URL, to the local destination
def download(url: str, filename: str, maintainer: str):
    file_path = os.path.join(destination_dir, filename)
    print('Downloading', url)
    r = requests.get(url, stream=True)
    if r.ok:
        print('saving to', os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())

        sourceJson = {}
        with open(file_path) as f:
            try:
                sourceJson = json.load(f)
                # Add maintainer field to each template
                for t in sourceJson.get('templates', []):
                    t['maintainer'] = maintainer

            except json.decoder.JSONDecodeError as err:
                print(f'Skipping one of the sources due to an error: {f.name}')
                print(f'Error msg: {err.msg}')

        if not sourceJson:
           return

        with open(file_path, 'w') as f:
            json.dump(sourceJson, f, indent=2, sort_keys=False)

    else:  # HTTP status code 4XX/5XX
        print('Download failed: status code {}\n{}'.format(r.status_code, r.text))

# Gets list of URLs to download from CSV file
def get_source_list():
  sources=[]
  with open(sources_list, mode='r') as file:
      csvFile = csv.reader(file)
      for lines in csvFile:
        if len(lines) > 1 and lines[1].strip():
          sources.append(lines)
  return sources

# Create destination folder if not yet present
if not os.path.exists(destination_dir):
  os.makedirs(destination_dir)

# For each source, download the templates JSON file
for sourceUrl in get_source_list():
  download(sourceUrl[1], sourceUrl[0] + '.json', sourceUrl[2])
