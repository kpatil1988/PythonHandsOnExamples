f = open(r"C:\Users\karthik.patil\Desktop\MyDocs\Learning\Python\WS\PythonHandsOnExamples\employees.csv","r")
data = f.readlines()
for n,row in enumerate(data):
    if n != 0:
        list_temp = row.split(',')
        if list_temp[1]== 'Male' and list_temp[0] != '':
            print(list_temp[0])
f.close()