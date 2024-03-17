import csv

with open('test_1_1_home_search.csv', 'r', encoding='utf8') as f:
    data = csv.reader(f)
    print(data)
    for i in data:
        print(i)