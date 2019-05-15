f = open(r"C:\Users\karthik.patil\Desktop\MyDocs\Learning\Python\WS\PythonHandsOnExamples\employees.csv","r")
data = f.readlines()
total_salary = 0;
count_emp = 0;
list_salary = list()
for n,row in enumerate(data):
    if n != 0:
        list_temp = row.split(',')
        if list_temp[1] =='Female' and list_temp[6] == 'TRUE':
            print(list_temp[0])
