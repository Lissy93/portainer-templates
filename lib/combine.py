import json
import os
import string

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SOURCES_DIR = os.path.join(BASE_DIR, 'sources')

LOCAL_SOURCES = {'lissy93_templates.json', 'example_templates.json'}

TYPE_LABELS = {1: 'container', 2: 'swarm', 3: 'stack', 4: 'kubernetes'}

reset_color = "\033[0m"
def rgb(r, g, b):
  return f"\033[38;2;{r};{g};{b}m"

def normalize_string(original, lowercase=True):
  normalized = original.translate(str.maketrans('', '', string.punctuation)).replace(' ', '')
  return normalized.lower() if lowercase else normalized.capitalize()

def template_score(t):
  """Score a template's completeness. Higher is more complete."""
  score = len(t)  # number of top-level keys
  score += len(t.get('env', []))
  score += len(t.get('volumes', []))
  score += len(t.get('ports', []))
  return score

def load_sources():
  """Load and merge all template JSON files from the sources directory."""
  templates = []
  for file in sorted(os.listdir(SOURCES_DIR)):
    file_path = os.path.join(SOURCES_DIR, file)
    if not (os.path.isfile(file_path) and file.endswith('.json')):
      continue
    with open(file_path) as f:
      try:
        source_templates = json.load(f)['templates']
      except (json.decoder.JSONDecodeError, KeyError) as err:
        print(f'{rgb(255, 0, 0)}Skipping source due to error:{reset_color} {f.name}')
        print(f'Error: {err}')
        continue
    for t in source_templates:
      t['_source'] = file
    templates += source_templates
  return templates

VALID_ENV_KEYS = {'name', 'label', 'description', 'default', 'preset', 'select'}

def normalize_template_fields(templates):
  """Fix non-standard field names and malformed entries from upstream sources."""
  for t in templates:
    # Merge singular 'category' into 'categories'
    if 'category' in t:
      existing = t.get('categories', [])
      merged = list(dict.fromkeys(existing + t.pop('category')))
      t['categories'] = merged

    # Fix env vars
    if 'env' in t:
      cleaned_env = []
      for env in t['env']:
        # Filter malformed entries (entire templates nested in env arrays)
        if not isinstance(env.get('name'), str) or any(k in env for k in ('categories', 'repository', 'logo')):
          continue
        # Convert non-standard 'set' to 'default' + 'preset'
        if 'set' in env and 'default' not in env:
          env['default'] = env.pop('set')
          env.setdefault('preset', True)
        elif 'set' in env:
          del env['set']
        cleaned_env.append(env)
      t['env'] = cleaned_env

    # Fix volume 'read_only' -> 'readonly' (and coerce to bool)
    for vol in t.get('volumes', []):
      if 'read_only' in vol:
        val = vol.pop('read_only')
        vol['readonly'] = val if isinstance(val, bool) else str(val).lower() == 'true'

def is_valid_template(t):
  """Check a template has the required fields for its type."""
  if not isinstance(t.get('title'), str) or not isinstance(t.get('description'), str):
    return False
  tmpl_type = t.get('type', 1)
  if tmpl_type == 1 and 'image' not in t:
    return False
  if tmpl_type in (2, 3) and 'repository' not in t:
    return False
  return True

def deduplicate_and_normalize(templates):
  """Filter invalid, deduplicate by (title, type) keeping best version, and normalize category names."""
  best = {}
  for t in templates:
    if not is_valid_template(t):
      print(f'{rgb(255, 165, 0)}Skipping invalid template:{reset_color} {t.get("title", "<no title>")}')
      continue
    key = (normalize_string(t['title']), t.get('type', 1))
    t_is_local = t.get('_source') in LOCAL_SOURCES
    t_score = template_score(t)
    if key in best:
      existing = best[key]
      existing_is_local = existing.get('_source') in LOCAL_SOURCES
      existing_score = template_score(existing)
      # Local always beats non-local; among same locality, higher score wins
      if t_is_local and not existing_is_local:
        best[key] = t
      elif not t_is_local and existing_is_local:
        pass  # keep existing
      elif t_score > existing_score:
        best[key] = t
    else:
      best[key] = t
  result = []
  for t in best.values():
    t['categories'] = list(dict.fromkeys(
      normalize_string(c, lowercase=False) for c in t.get('categories', [])
    ))
    result.append(t)
  return result

def postfix_ambiguous_titles(templates):
  """Append type labels to titles that appear with multiple types."""
  from collections import Counter

  # Pass 1: postfix titles that share a normalized name across different types
  title_counts = Counter(normalize_string(t['title']) for t in templates)
  ambiguous = {title for title, count in title_counts.items() if count > 1}
  for t in templates:
    if normalize_string(t['title']) in ambiguous:
      tmpl_type = t.get('type', 1)
      label = TYPE_LABELS.get(tmpl_type, f'type{tmpl_type}')
      t['title'] = f"{t['title']} ({label})"

  # Pass 2: postfix any NEW collisions created by pass 1
  post_counts = Counter(normalize_string(t['title']) for t in templates)
  new_ambiguous = {title for title, count in post_counts.items() if count > 1}
  for t in templates:
    if normalize_string(t['title']) in new_ambiguous and not t['title'].endswith(')'):
      tmpl_type = t.get('type', 1)
      label = TYPE_LABELS.get(tmpl_type, f'type{tmpl_type}')
      t['title'] = f"{t['title']} ({label})"

if __name__ == '__main__':
  raw = load_sources()
  normalize_template_fields(raw)
  templates = deduplicate_and_normalize(raw)
  postfix_ambiguous_titles(templates)
  # Strip internal _source tag
  for t in templates:
    t.pop('_source', None)
  templates.sort(key=lambda t: t['title'].lower())
  for i, t in enumerate(templates, start=1):
    t['id'] = i
  output = {'version': '3', 'templates': templates}
  with open(os.path.join(BASE_DIR, 'templates.json'), 'w') as f:
    json.dump(output, f, indent=2, sort_keys=False)
