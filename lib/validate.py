import json
import os
import sys
from jsonschema import validate, ValidationError

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.join(script_dir, '..')

    try:
        schema = load_json_file(os.path.join(root_dir, 'Schema.json'))
        templates = load_json_file(os.path.join(root_dir, 'templates.json'))
        validate(instance=templates, schema=schema)
        print('✅ templates.json is valid against the schema')
    except ValidationError as ve:
        print(f'❌ Validation error: {ve.message}')
        if isinstance(ve.instance, dict):
            print(f'   Title of invalid template: {ve.instance.get("title")}')
        sys.exit(1)
    except FileNotFoundError as fnfe:
        print(f'❌ File not found: {fnfe}')
        sys.exit(1)
    except json.JSONDecodeError as jde:
        print(f'❌ JSON decoding error: {jde}')
        sys.exit(1)

if __name__ == '__main__':
    main()
