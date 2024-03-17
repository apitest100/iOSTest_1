import yaml

with open('my_yaml_3.yml', 'r', encoding='utf8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
    print(data['jd']['appium:platformName'])
    print(data['jd']['appium:platformVersion'])
    print(data['jd']['appium:deviceName'])
    print(data['jd']['appium:udid'])
    print(data['jd']['appium:bundleId'])