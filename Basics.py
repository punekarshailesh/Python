''' translator work is to convert HLL to LLL by using either compiler or interpreter

    Simple and easy
    free & open source
    HLL , Developed by Guido van Russum
    Portable

    ** Always remember of indentation/proper spacing in python

'''
# to check system python version
import sys
print("Python version : "+ sys.version)


# for single line comment
''' Multi line comments '''

print("Hello world") 


print("Hi My name is shailesh",",", "I am Learning Python for Data Science")

# print("Hi",end="","Hello") - Error

print("I am shailesh maroti madne,",end="")
print("Currently pursing graduation from NIT Calicut")

# variables

Name = "Shailesh Maroti Madne"
print(Name)

age = 33
print(age)

price = 23.343
print(price)

# assignment operator (=) 

# Rules for identifiers
# 1.
myVar = 39
Var_2 = 39488.985875
P_ = 'hi'
print(myVar , Var_2, P_)

# 2. Variable/identifiers name cannot start with digit eg. 3_var invalid naming for variable or identifiers
# 3. Cannot use special symbols like $, @, # etc. in identifiers eg. age_$ invalid
# 4. it can be of any length 
myPersonalPhoneNumberIs = 9850853
print(myPersonalPhoneNumberIs)


# type() - to get the type of the variables/identifiers
print(type(myPersonalPhoneNumberIs),type(Var_2), type(P_))

''' Data types
             Integers - +ve, -ve , 0
             strings - Collection of characters
             Float - decimal values
             boolean - True / False
             None
''' 
Val  = True
a = None
print(type(Val), type(a))


# float - decimal values

# Boolean - True / False

# None

def func():
    return None



print(type(func()))



'''
        Keywords

        and , as , None , True, False, is , in , return, lambda, not, or, pass, raise, yield, while, with, try, import, if, global, from, for, finally, except, else, continue, def, del, elif, class, break, assert 
'''

# Case sensitive - A and a different


# Arithmetic - (*, /, + , - , **, %)
# ** - Power , % remainder
a = 5
b = 3

print(a+b)
print(a-b)
print(a/b) # / this divide will give floating value
print(a//b) # // this dividde will give integer
print(a*b)
print(a**b) # a**b = a^b
print(a%b)


# Relational - (!= , ==, >, <, >= , <=)

print(a>b)
print(a<b)
print(a!=b)
print(a==b)
print(a>=b)
print(a<=b)

# Assignment - (+= , *= , /= , -=, = , %= , **=)

a += b # a = a+b = 8
print(a)
a -= b # a = a-b = 5
print(a)

# print(a/=b)  - invalid syntax
# a /= b # a = a/b = 1.666
# print(a)

a **= b # a = a^b = 5^3
print(a)

a %= b # a = a%b = 125%3 
print(a)


# Logical (not(!) , and(&) , or(|)) - works on bolean values


print(a and b) # True
print(a or b)  # False
print(not a)    # False
print(not b)    # False

# Type conversion - automatically converted
# Type casting - manually converted by user

'''Type conversion
    VALID CASES :
        int + int 
        int + float
        float + float
        float + int
        string + string

    INVALID CASES :
        int + string
        float + string

'''
a , b = 1 , 3.553
sum = a + b
print(sum)
print(type(sum))
x , y = "2", "3"
print(x+y)

'''Type Casting 

        INVALID CASES i.e. adding string to int/float can be done by type casting

'''
a , b = 2 , "3"

# sum = a + b -> INVALID
sum = a + float(b)
print(sum)



'''
        Conditional statements

        if
        if-else
        if-elif-else

'''
 
age = int(input("Enter your age: "))

# if-else
if(age >= 18):
    print("You'r eligible to vote!")
    print("You can drive!")
else:
    print("You'r not eligible to vote!")


# if-elif-else
signal_light = input("Enter signal light: ")

if(signal_light == 'Red' or signal_light == 'red' or signal_light == 'RED'):
    print("Stop the car!")
elif(signal_light == 'Green' or signal_light == 'green' or signal_light == 'GREEN'):
    print("You can drive")
elif(signal_light=='Yellow' or signal_light=='yellow' or signal_light=='YELLOW'):
    print("Slow down!")
else:
    print("Go to hell !")


'''
        Nesting 

        if condition1:
            if condition2:
                if condition3:
                    if condition4:
'''
if age > 18:
    if age >= 18 and age <= 40:
        print("You'r citizen of india")
    else:
        print("You'r senior citizen of india")
else:
    print("You'r aadhar is not valid")    


