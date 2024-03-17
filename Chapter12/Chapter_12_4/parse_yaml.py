import yaml

'''
1、parse_yaml函数有3个参数：
（1）file，文件名
（2）section，段落名
（3）Key，键名。如果不传递key，则返回整个字典，如果传递key，则返回单个key值
'''
def parse_yaml(file, section, key=None):
    with open(file, 'r', encoding='utf8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if key==None:
            return data[section]
        else:
            return data[section][key]



if __name__ == '__main__':
    value = parse_yaml('my_yaml_3.yml', 'jd', 'appium:platformName')
    all_value = parse_yaml('my_yaml_3.yml', 'jd')
    print(value)
    print(all_value)