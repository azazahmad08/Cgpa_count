# Using This application you can convert your sgpa to cgpa
# Azaz Ahmad Swapnil
# Please do not edit or modify this code


Semester1 = float(input("Enter your Sgpa:"))
Semester2 = float(input("Enter your Sgpa:"))
Semester3 = float(input("Enter your Sgpa:"))
Semester4 = float(input("Enter your Sgpa:"))
Semester5 = float(input("Enter your Sgpa:"))
Semester6 = float(input("Enter your Sgpa:"))
Semester7 = float(input("Enter your Sgpa:"))
Semester8 = float(input("Enter your Sgpa:"))
avg = (Semester1+Semester2+Semester3+Semester4+Semester5+Semester6+Semester7+Semester8)
total_semester = int(input("Enter your total semester number :"))
result = float(avg) / int(total_semester)
cgpa = "{:.2f}".format(result)
print("Your result is :", cgpa,)

'''
Azaz Ahmad Swapnil
Computer Science & Engineering Department
3rd year Student
Daffodil International University
'''
