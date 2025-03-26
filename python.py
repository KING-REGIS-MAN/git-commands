#a = 20
#b = 30
#print(a+b)
#print('5667')
#x = 2; y = 3; l = [0,1,2]
#if #(1<x<=3 and 4>y>=2) or (1==1 or 0!=1) or 1 in l:
#if 1 in l:
 #  print('Hello World')
#print("Values")
#age = input('Enter Age:')
#age = 12
#age = int(age)+2
#print(age)


#######
#name = input("Enter your name:")
#print('Hello ' +name)

Foo = (1, 1, 2, 2, 3, 3)  # Use commas to separate tuple elements
Foo = ()  # This overwrites the previous tuple, is this intentional?
#print(len(Foo))  # Use 'len' instead of 'ten' and fix capitalization
###########

students = {'firstname': 'John', 'lastname': 'Regis', 'age': 21}   #### THIS IS A LIST CALLED "students", IT CONTAIN DIFFERENT KEYS AND THEIR VALUES.
print(students['firstname']) #--KEYS AND VALUES
print(students['lastname'])  #--KEYS AND VALUES
print(students['age'])  #--KEYS AND VALUES
studies = {1: 'Aaron', 2: 'John', 3: 'Charlie'}  ##--CREATED A LIST CALLED STUDIES
print(studies[1]) #The name of the key
students ['Firstname'] = {'Samuel', "John", 'Regis'}  # Updating a dictionary
print(students)
print(students.items())  #prints out all the items in students
print(students.keys())  #prints out the key in the dict(students)
print(students.values())  #prints out the values in the dict(students)
newstudents = students.copy()  ##--It copies the information or everyting from students into newstudents
print(newstudents) ##This will bring the output
students.clear()  ##Clears everthing from students
print(newstudents) 
newstudents.update({'Department': 'SQL'})  # Append a dictionary
print(newstudents)


Data = {34, 10, 39, 38, 20}
Data.sort()
Data.reverse()
print(Data)


#import os

#for root, dirs, files in os.walk("C:/Users"):
    #print("Current Directory:", root)
    #print("Subdirectories:", dirs)
    #print("Files:", files)
