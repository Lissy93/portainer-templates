import json
import urllib.parse
import os
import csv
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
readme_path = os.path.join(project_dir, '.github/README.md')
templates_path = os.path.join(project_dir, 'templates.json')
sources_path = os.path.join(project_dir, 'sources.csv')

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def load_csv_file(file_path):
    with open(file_path, 'r') as file:
        return list(csv.reader(file))

def slugify(title: str):
    baseUrl = 'https://portainer-templates.as93.net'
    return f'{baseUrl}/{re.sub(r"[^a-zA-Z ]", "", title.lower()).replace(" ", "-")}'

def generate_app_list():
  templates = load_json_file(templates_path)['templates']
  templates.sort(key=lambda template: template['title'].lower())
  markdown_content = ''
  for index, template in enumerate(templates):
      name = template['title'].title()
      description = re.sub('[^0-9a-zA-Z]+', ' ', (template['description'] or ''))
      if 'logo' in template and template['logo']:
          logo = f"<img title=\"{description}\" src='{template['logo']}' width='26' height='26' /> "
      else:
          logo = ' '      
      markdown_content += f"{index+1}. {logo}**[{name}]({slugify(name)} '{description}')**\n"
  return markdown_content

def generate_sources_list():
    sources = load_csv_file(sources_path)
    markdown_content = ''
    
    for index, source in enumerate(sources):
        if len(source) > 1 and source[1].strip():
          url = source[1].strip()
          parsed_url = urllib.parse.urlparse(url)
          username = parsed_url.path.split('/')[1]
          avatar = f'<img src="https://github.com/{username}.png?size=40" width="26" height="26" />'
          markdown_content += f"{index + 1}. {avatar} [template]({url}) by [@{username}](https://github.com/{username})\n"
    
    return markdown_content

def insert_content_between_markers(file_path, start_marker, end_marker, content_to_insert):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    start_index = -1
    end_index = -1

    for i, line in enumerate(lines):
        if start_marker in line:
            start_index = i
        if end_marker in line:
            end_index = i
            break

    if start_index >= 0 and end_index >= 0:
        lines[start_index + 1:end_index] = [content_to_insert + '\n']

    with open(file_path, 'w') as file:
        file.writelines(lines)

# Insert sources list into readme
insert_content_between_markers(
  readme_path,
  '<!-- auto-insert-sources:start -->',
  '<!-- auto-insert-sources:end -->',
  generate_sources_list(),
)

# Insert app list into readme
insert_content_between_markers(
  readme_path,
  '<!-- auto-insert-apps:start -->',
  '<!-- auto-insert-apps:end -->',
  generate_app_list(),
)
