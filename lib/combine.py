import os
import string
import json

# Source: https://ask.replit.com/t/how-do-i-make-colored-text-in-python/29288/18
reset_color = "\033[0m" # Important!
def rgb(r, g, b):
  return f"\033[38;2;{r};{g};{b}m"

# Get list of files in sources
dir = os.path.dirname(os.path.abspath(__file__))
templates_src_dir = os.path.join(dir, '../sources/')
template_dest_file = os.path.join(dir, '../templates.json')

files = os.listdir(templates_src_dir)

# Initialize empty list to store template objects
templates = []

# For each file in sources
for file in files:
  file_path = os.path.join(templates_src_dir, file)
  if os.path.isfile(file_path) and file.endswith('.json'):
    with open(file_path) as f:
      try:
        # Load the JSON into a variable
        data = json.load(f)['templates']
        # Append the template object to the templates list
        templates = templates + data
      except json.decoder.JSONDecodeError as err:
        print(f'{rgb(255, 0, 0)}Skipping one of the sources due to an error:{reset_color} {f.name}')
        print(f'Error msg: {err.msg}')

seen_titles = set()
filtered_data = []

def normalize_string(original, lowercase = True):
  normalized = original.translate(str.maketrans('', '', string.punctuation)).replace(' ', '')
  return normalized.lower() if lowercase else normalized.capitalize()

for x in templates:
    normalized_title = normalize_string(x['title'])
    if normalized_title in seen_titles:
        continue

    seen_titles.add(normalized_title)
    filtered_data.append(x)

    categories = x.get('categories', [])
    x['categories'] = []

    for category in categories:
      normalized_category = normalize_string(category, lowercase = False)

      if normalized_category not in x['categories']:
        x['categories'].append(normalized_category)

fileData = {
  'version': '2',
  'templates': filtered_data
}

# Open the templates.json file, and write results to it
with open(template_dest_file, 'w') as f:
  json.dump(fileData, f, indent=2, sort_keys=False)
