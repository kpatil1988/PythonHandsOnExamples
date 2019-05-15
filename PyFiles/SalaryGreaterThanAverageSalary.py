f = open(r"C:\Users\karthik.patil\Desktop\MyDocs\Learning\Python\WS\PythonHandsOnExamples\employees.csv","r")
data = f.readlines()
total_salary = 0;
count_emp = 0;
list_salary = list()
for n,row in enumerate(data):
    if n != 0:
        list_temp = row.split(',')
        total_salary+= int(list_temp[4])
        list_salary.append(int(list_temp[4]))
        count_emp = n-1

average_salary = total_salary//count_emp
print(average_salary)
for n,row in enumerate(data):
    if n != 0:
        list_temp = row.split(',')
        if int(list_temp[4])>average_salary :
            print(list_temp[0])

