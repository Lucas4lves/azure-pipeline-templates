import yaml

with open('./sonar-scanner.yml', 'r') as file:
    yaml_parser = yaml.safe_load(file)

print(yaml_parser)
