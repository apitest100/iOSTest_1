import yaml

with open('my_yaml_2.yml', 'r', encoding='utf8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)