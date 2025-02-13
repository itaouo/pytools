import json
from lib.CustomException import Fail, Success
from deepdiff import DeepDiff

def format_json_string(content, indentation = '  '):
    indent = ''
    i = 0

    content = content.replace('\n', '')
    content = content.replace(' ', '')

    content = list(content)
    while i < len(content):
        if content[i] == '{' or content[i] == '[':
            indent += indentation
            content[i+1:i+1] = indent
            content.insert(i + 1, '\n')
            i += len(indent) + 1
        elif content[i] == '}' or content[i] == ']':
            indent = indent[0:len(indent)-2]
            content[i:i] = indent
            content.insert(i, '\n')
            i += len(indent) + 1
        elif content[i] == ',':
            content[i+1:i+1] = indent
            content.insert(i + 1, '\n')
        elif content[i] == ':':
            content.insert(i + 1, ' ')
        i += 1
    return ''.join(content)

def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except json.JSONDecodeError as e:
        return False

def invalid_json(json_str):
    try:
        json.loads(json_str)
    except json.JSONDecodeError as e:
        return str(e)

def json_differences(json_str_1, json_str_2):
    dict1 = json.loads(json_str_1)
    dict2 = json.loads(json_str_2)

    diff = DeepDiff(dict1, dict2)
    if not diff:
        raise Success("Jsons are the same.")

    result = "\n\n"
    for key, change in diff.get('values_changed', {}).items():
        result += f"{key} | old: {change['old_value']} -> new: {change['new_value']}\n"

    for key in diff.get('dictionary_item_added', []):
        result += f"added from original: {key}\n"

    for key in diff.get('dictionary_item_removed', []):
        result += f"Removed from original: {key}\n"

    return result

class IsJsonValid:
    def execute(self):
        json_str = input("Enter the Json: ")
        if is_valid_json(json_str):
            raise Success("Json is valid.")
        else:
            raise Fail("Invalid Json", 
                f"{invalid_json(format_json_string(json_str))}\n{format_json_string(json_str)}")
        
class CompareJsons:
    def execute(self):
        json_str_1 = input("Enter the original Json: ")
        if not is_valid_json(json_str_1):
            raise Fail("Invalid Json", 
                f"{invalid_json(format_json_string(json_str_1))}\n{format_json_string(json_str_1)}")
        
        json_str_2 = input("Enter the changed Json: ")
        if not is_valid_json(json_str_2):
            raise Fail("Invalid Json", 
                f"{invalid_json(format_json_string(json_str_2))}\n{format_json_string(json_str_2)}")
        
        raise Fail("Mismatch Json", json_differences(json_str_1, json_str_2))
        