import tools
import yaml
import json

def yaml_load(filepath):
    """loads a yaml file"""
    with open(filepath, "r") as f:
        data = yaml.safe_load(f)
    return data

def yaml_dump(filepath, data):
    """dumps data into a yaml file"""
    with open(filepath, "w") as f:
        yaml.safe_dump(data, f)

def yaml_from_json(json_filepath):
    with open (json_filepath,'r') as stream:
        content = stream.read()
        content = json.loads(content)
        content = yaml.safe_load(content)
        return content
