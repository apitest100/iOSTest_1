import csv

'''
1、parse_csv函数有2个参数：file，文件名；startline，数据起始行；
2、file参数为必传参数；
3、startline为默认参数，默认值为1，即从第二行读取。因为，一般第一行为标题行
'''
def parse_csv(file,startline=1):
    mylist = []
    with open(file, 'r', encoding='utf8') as f:
        data = csv.reader(f)
        for i in data:
            mylist.append(i)
        if startline == 1:
            del mylist[0] # 删除标题那行数据
        else:
            pass
        return mylist


if __name__ == '__main__':
    data = parse_csv('test_1_1_home_search.csv')
    print(data)
    print(*data)