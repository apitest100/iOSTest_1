import yaml

with open('my_yaml_1.yml', 'r', encoding='utf8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
    print(data['appium:platformName'])
    print(data['appium:platformVersion'])
    print(data['appium:deviceName'])
    print(data['appium:udid'])
    print(data['appium:bundleId'])