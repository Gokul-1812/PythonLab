import csv
try:
    with open('test2.csv','w+',newline='') as outf:
        fieldnames=['Rollno','Name']
        content=csv.DictWriter(outf,fieldnames=fieldnames)
        content.writeheader()
        content.writerow({'Rollno':'1','Name':'Tom'})
        content.writerow({'Rollno':'2','Name':'Vivek'})
        content.writerow({'Rollno':'3','Name':'Jyo'})
        content.writerow({'Rollno':'4','Name':'Sarath'})
        print('test2.csv : ')
        outf.seek(0,0)
        print(outf.read())
except Exception as e:
    print(e)
