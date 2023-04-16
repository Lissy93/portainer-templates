import os
import json

# Get list of files in sources
dir = os.path.dirname(os.path.abspath(__file__))
templates_src_dir = os.path.join(dir, '../sources/')
template_dest_file = os.path.join(dir, '../templates.json')

files = os.listdir(templates_src_dir)

# Initialize empty list to store template objects
templates = []

# For each file in sources
for file in files:
    # Open the file
    with open(templates_src_dir + file) as f:
        # Load the JSON into a variable
        data = json.load(f)['templates']
        # Append the template object to the templates list
        templates = templates + data

# Remove duplicates
seen_titles = set()
filtered_data = [x for x in templates if x['title'] not in seen_titles and not seen_titles.add(x['title'])]

fileData = {
  'version': '2',
  'templates': filtered_data
}

# Open the templates.json file, and write results to it
with open(template_dest_file, 'w') as f:
  json.dump(fileData, f, indent=2, sort_keys=False)
