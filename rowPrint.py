import csv
try:
    with open('test1.csv') as f:
        content=csv.reader(f,delimiter=',')
        count=0
        for row in content:
            if count==0:
                print(f'Column names : {", ".join(row)}')
                col=int(input(('Enter column header number : ')))
                count=1
            else:
                print(row[col-1])
except Exception as e:
    print(e)
