import csv
try:
    with open('test.csv') as f:
        content=csv.reader(f,delimiter=',')
        count=0
        for row in content:
            if count==0:
                print(f'Column names : {", ".join(row)}')
                count=1
            else:
                print(f'{row[0]} of {row[1]} department is working in {row[2]}')
except Exception as e:
    print(e)
