import json
import os
import sys
from jsonschema import validate, ValidationError

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))

        schema_file = os.path.join(script_dir, '..', 'Schema.json')
        templates_file = os.path.join(script_dir, '..', 'templates.json')

        schema = load_json_file(schema_file)
        templates = load_json_file(templates_file)
        
        validate(instance=templates, schema=schema)
        
        print('✅ templates.json is valid against the schema')

    except ValidationError as ve:
        print('Validation error:', ve.message)
        sys.exit(1)
    except FileNotFoundError as fnfe:
        print(f'File not found error: {fnfe}')
        sys.exit(1)
    except json.JSONDecodeError as jde:
        print(f'JSON decoding error: {jde}')
        sys.exit(1)

if __name__ == '__main__':
    main()
