'''
    4 pillars of oops

    1. Abstraction :
        hiding the unecessary information from the user

    2. Encapsulation:
        wrapping the data and functions into a single unit(object)
'''

# Abstraction
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluch = False

    def Start(self):
        self.acc=True  # this hided from users (Abstraction)
        self.cluch=True # this hided from users (Abstraction)
        print("Car started..")
    

obj = Car()

obj.Start()


# Encapsulation - wrapping data and functions into a sinigle unit(object)


'''
    del keyword
        used to delete object properties/ object itself
'''


class Student:
    def __init__(self,name) -> None:
        self.name = name
    


s1 = Student("Shailesh")
print(s1.name)
# del s1 - deleted object
# print(s1) - error as s1 object deleted
del s1.name # delete the name attribute in object
print(s1)
# print(s1.name) - error


'''
    Private attribute / methods
        only accessible within class only
        not accessible outside class
        __ is used to make attribute private
'''
# private attributes
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # acc_pass is private attribute

    # setter - setting / resetting the password
    def reset_password(self, newPassword):
        self.__acc_pass = newPassword

    

ac1 = Account(1357543,'Shailesh@29')
print(ac1.acc_no)
# print(ac1.__acc_pass) - > Error as acc_pass is private member of the class not accessible outside the class

ac1.reset_password("Shailesh@35")

print()

# private methods - accessible only inside class

class Person:
    def __hello(self):
        print("hello world")

    # __hello() function accessible inside class
    def welcome(self):
        self.__hello()

P = Person()
# P.__hello() - private function not accessible outside class
P.welcome()


'''
    3. Inheritance
        Inheriting the properties of another class
        class1:
        class2:

        class1 (Parent) --> class2 (Child) inherite the properties of class1
'''

# Understanding Single Inheritance
class Car:
    color = 'black'
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

# here toyota class inherite the properties of class - Car
class Toyota(Car):
    def __init__(self, name):
        self.name = name
    

car1 = Toyota("Fortuner")
car2 = Toyota("porche")

print(car1.name)

car1.start() # no errors as we have inherited     

print(car1.color)


''' 
     Multi-level Inheritance

        Car (class 1) Parent1
            |
        Toyota (class 2) Child of Parent1 and parent for Design class
            |   
        Fortuner (class 3) Child of Parent class -Toyota and grand child for Car class
'''
class Fortuner(Toyota):
    def __init__(self, type):
        self.type = type
        # pass

obj = Fortuner("Petrol") # created object for fortuner class

print(obj.type)
obj.start()

obj.stop()

print(obj.color)


'''
    Multiple Inheritance
        one class can inherits multiple classes
'''

class A:
    varA = "welcome to class A"
class B:
    varB = 'welcome to class B'

class C(A, B):
    varC = 'welcome to class C'


obj1 = C()
print(obj1.varA)
print(obj1.varB)
print(obj1.varC)

'''
    Super() 
        -> methods used to acces the method of the parent class
'''
class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print('car started..')


class Toyota(Car):
    def __init__(self, name, type):
        self.name = name
        # to set type in parent class
        super().__init__(type)



car1 = Toyota("prius","electric")
print(car1.type)


'''
    Class method
        A class method is bound to the class & receives the class as an implicit 

        __class__.attr
        className.attr

        @classmethod
        def func(cls): # cls - class
            pass
'''

class Person:
    name = "anonymous"
    # def changeName(self, name):
        # pass
    #     self.name = name 
    #     # Person.name = name  --> changes class attribute name anonymous to Rahul Kumar   
    #   self.__class__.name = name --> another method to change class attribute name 'anonymours' to 'Rahul Kumar'
    
    # change by using @classmethod
    @classmethod
    def changeName(cls, name):
         cls.name = name # change the class attribute name anonymour to rahul kumar



p1 = Person()
p1.changeName("Rahun Kumar")
print(p1.name)
print(Person.name)


'''
    @property method
'''
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    
    @property
    def percentage(self):
        return str((self.phy + self.math + self.chem)/3)+"%"
        

stu1 = Student(98,97,99)
print(stu1.percentage)

stu1.phy = 87
print(stu1.percentage)


'''
    Polymorphism - Operator Overloading
    when the same operator is allowed to have different meaning according to the context

'''

# Here in below codes + is acting as OverLoaded Operator 
print(1 + 3 ) # 4
print("apna"+"college") # concat
print([1,3,5]+[2,4,6]) # combine 2 list - merge


