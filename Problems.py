# # a = int(input())
# # b = int(input())

# # print(a+b)


# # side = float(input("Enter side of square: "))

# # area = side**2
# # print("Area of square: ",area)



# # # Q.

# # first_name = input("Enter first Name: ")
# # print(len(first_name))


# # # Q.

# # input_string = input()
# # print(input_string.count('$'))


# # # Q.
# # num = int(input("Enter a number: "))

# # if num%2 == 0:
# #     print("Even")
# # else:
# #     print("Odd")

# # # Q.
# # a = int(input())
# # b = int(input())
# # c = int(input())

# # if a > b:
# #     if a > c:
# #         print("a is greater")
# #     else:
# #         print("c is greater")
# # else:
# #     if b > c:
# #         print("b is greater")
# #     else:
# #         print("c is greater")


# # # Q.

# # num = int(input("Enter a number: "))
# # if num%7 == 0:
# #     print(num, " is multiple of 7")
# # else:
# #     print(num, " is not multiple of 7")


# # # Q. Find largest of 4 numbers
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# if a > b and a > c and a >d:
#     print("a is greater")
# elif b > c:
#     if b > d:
#         print("b is greater")
#     else:
#         print("d is greater")
# else:
#     if c > d:
#         print("c is greater")
#     else:
#         print("d is greater")

# # Q. largest of 5 number
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# if a > b and a > c and a > d and a > e:
#     print("a is greater")
# elif b > c:
#     if b > d and b > e:
#         print("b is greater")
#     else:
#         if d > e:
#             print("d is greater")
#         else:
#             print("e is greater")
# else:
#     if c > d :
#         if c > e:
#             print("c is greater")
#         else:
#             print("e is greater")
#     elif d > e:
#         print("d is greater")
#     else:
#         print("e is greater")




# # # Q. input 3 movies and store in list

# # movie = []

# # for i in range(3):
# #     x = input("Enter movie name: ")
# #     movie.append(x)

# # print(movie)


# # Q. check whether list is palindrome or not
# number = [1, 2, 3, 2, 3]
# List = number.copy()


# List.reverse()
# print(List)

# if List == number:
#     print("Palindrome")
# else:
#     print("not a palindrome")


# # Q. count the number of students with grade 'A'

# t = ("C", "D", "A", "A", "B", "B", "A")
# print(t.count("A"))

# # Q. store in list and sort
# List = []

# for i in t:
#     List.append(i)
    
# List.sort()
# print(List)


# # Q. store words meaning in dictionary

# meaning = {
#     "table" : ["a piece of furniture","list of facts & figures"],
#     "cat" : "a small animal"
# }
# print(meaning)


# # Q. count the number of classrooms
# subjects = {"python", "java", "C++", "python","javascript","java","python","java","C++","C"}

# print(subjects)
# print("Number of classrooms needed: ",len(subjects))


# # store inputed subject name and marks in dictionary

# # dict = {}

# # number = 3
# # for i in range(number):
# #     sub = input("Enter your subject: ")
# #     marks = float(input("Enter your marks: "))
# #     # dict[sub] = marks
# #     dict.update({sub : marks})

# # print(dict)


# # Q. store 9 and 9.0 in set as separate values
# values = {9, '9.0'} # python treat 9 and 9.0 equal
# print(values)

# values = {("float",9.0),("int",9)}
# print(values)



# ''' Questions on LOOPS  '''

# # Q print from 100 to 1
# i = 100 
# while i>=1:
#     print(i)
#     i -= 1
# print("Loop ended")


# # printing list elements
# List = [1, 4, 9 , 16, 25, 36, 49, 64, 81, 100]

# i = 0
# while i<len(List):
#     print(List[i])
#     i += 1


# # Q. search value in tuple
# values = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,25)
# x = int(input("Enter value to search: "))

# i = 0
# while i<len(values):
#     if(values[i] == x):
#         print('value found at index',i)
#     else:
#         print("Finding....")
#     i += 1


# # Q. print multiplication of a number n
# n = int(input("Enter a number: "))

# i = 1 
# while i<=10:
#     print(n, "X" , i , "=" , n*i)
#     i+=1



# # 100 to 1
# for i in range(100, 1,-1):
#     print(i)


# # multiplicatin table
# for i in range(1,11):
#     print(3*i)


# # Q. sum of first n - numbers
# n = int(input("Enter a number: "))

# i, sum = 0,0
# while i<=n:
#     sum += i
#     i += 1
# print(sum)


# # Q. Factorial of a number
# n = int(input("Enter a number: "))

# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print("factorial of",n,"is: ",fact)



# Q. print the elements of a list in a single line

List = [1, 3, 4, 5]
for items in List:
    print(items,end=" ")


# Q. find factorial of n
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact


n = int(input("Enter a num: "))
print(fact(n))



# Conver USD to INR 1usd = 80 rs

# def USD_INR(USD):
#     return USD*80

# print(USD_INR(45),"Rs")


# # check number even or odd
# def func(num):
#     if(num&1 == 0):
#         return "EVEN"
#     else:
#         return "ODD"
    
# print(func(5))
    


# # Problems related with file I/O

# # Q. create file and add the data


# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")


# # Q. replace the occurrences of the Java with Python

# with open("practice.txt","r") as f:
#     data = f.read()

# data = data.replace("Java","Python")

# print(data)

# with open("practice.txt","w") as f:
#     f.write(data)


# # Q. Find the word is present or not?
# ans = data.find("Pyhon")
# print(ans)
# if ans != -1:
#     print("word is  present")
# else:
#     print("word is not present")

# Q. find in which line the word is present?
# def check_line_num():
#     word = input("Enter : ")
#     line_no = 1
#     data = True
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if word in data:
#                 return line_no
#             line_no += 1
#     return -1

# print(check_line_num())
    


# Q. file contains the comma separated numbers, print the count of the even numbers.


# with open("file.txt","r") as f:
#     data = f.read()
#     data = data.split(",")
#     print(data)
#     count = 0
#     for items in data:
#         if int(items)&1 == 0:
#             count += 1
        
#     print("Number of even numbers in data: ",count)


# print(1 & 3)

# classes and objects

class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        # self.__marks2 = marks2
        # self.marks3 = marks3 
    
    def printValues(self):
        for i in range(len(self.marks)):
            print(self.marks[i], " ")
        
    # to print the average
    def getAverage(self):
        Sum = 0
        for i in range(len(self.marks)):
            Sum += self.marks[i]
        print("hi",self.name,"your avg score is : ",Sum/3)
        


obj = Student("Shailesh",[40,50,60])
obj.getAverage()
# print(obj.printValues())
obj.name = "tony stark"
obj.getAverage()

'''
Q. Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit and printing the balance
'''

class Account:
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self.balance = balance
    

    # debit - 
    def debit(self, debit_amount):
        if self.balance > debit_amount:
            self.balance -= debit_amount
            print(f"Amount debited:{debit_amount}Rs.")
            print(f"Total amount: {self.get_Balance()}Rs.")
        else:
            print("Insufficient Balance.")
    

    # Credit -
    def Credit(self, credit_amount):
        self.balance += credit_amount
        print(f"Amount credited:{credit_amount}Rs.")
        print(f"Total amount: {self.get_Balance()}Rs.")
    
    # Printing the balance
    def get_Balance(self):
        # print(f"Amount : {self.balance}Rs.")
        return self.balance


acc1 = Account(358374949, 1000000)
print("Amount present:",acc1.get_Balance())

acc1.debit(5000)
# print(acc1.get_Balance())
acc1.debit(5000000)
# print(acc1.get_Balance())
acc1.Credit(50000)
# print(acc1.get_Balance())


# Q. Circle - class radius - r Area() - return area and Perimeter() - return permiter

import math as mt
class Circle:
    def __init__(self, r):
        self.r = r
    
    def Area(self):
        return mt.pi * self.r * self.r
    
    def Perimeter(self):
        return 2 * mt.pi * self.r

obj1 = Circle(2)
print(f"Area : {format(obj1.Area(),'.2f')}")
print(f"Perimeter: {format(obj1.Perimeter(),'.2f')}")



'''
Q. define a Employee class with attributes role, department & salary. 
this class also had showDetails() method
create an Engineer class that inherite properties from Employee & 
'''