import yaml
import sys 

file_path = sys.argv[1]

with open(file_path, 'r') as file:
    yaml_parser = yaml.safe_load(file)

print(yaml_parser)
