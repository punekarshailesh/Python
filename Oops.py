'''Oops - object oriented programming

    ->  redundancy reduced
    ->  reusability increases

'''

# class Student:
#     name = "Shailesh Madne"


# # creating an instance(Object)
# s1 = Student() # student1

# print(s1)
# print(s1.name)

# s2 = Student() # student 2
# print(s2.name)


# class Car:
#     color='blue'
#     brand="Mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand) 


'''
    Constructor - __init__ 
'''

class College:
    name = "Karan"

    # # deafult constructors(only self) - no need to create this constructor
    # def __init__(self):
    #     pass 

    college_name = "NIT Calicut"
    # name = "anonymous"  # class attribute
    # parameterized constructors(self with other parameters)
    def __init__(self , name, branch):
        print("Adding new students in Database...")
        # self.name is new variable created in object
        self.name =  name  # object attribute > class attribute
        self.branch = branch

s1 = College("Shailesh Maroti Madne","CSE")
print(s1.college_name,s1.name,s1.branch)

''' 
    Class Attribute
        -> accessing class attribute using class name
        -> can be accessed using class_name.attribute or object_name.attribute


    Object attribute 
        -> accessed using the object.attribute

'''
print(College.college_name)
s2 = College("Prathmesh Gaikwad","Mech")
print(College.college_name, s2.name,s2.branch)

'''
    Methods :
        functions that belong to objects.
    Class = methods + attributes
'''

class XYZ:
    def __init__(self,name,rollNo):
        self.__name = name
        self.__rollNo = rollNo
    '''
        It is important in any methods it is important to pass first 
        first parameter as self
    '''
    def greetings(self):
        return "Welcome Students"
    
    # getter - get the value
    def get_name(self):
        return self.__name

    def get_rollNo(self):
        return self.__rollNo
        # return None 
    
    # setter - to set the value
    

obj1 = XYZ("Shailesh","B200849CS")
print(obj1.greetings())
print(obj1.get_name())
print(obj1.get_rollNo())

obj2 = XYZ("Prathmesh","B200857CS")


'''
    Static methods :
        don't use self parameter(work at class level) 
    Inside class without 'self' parameter
    for static methods we use (@staticmethod before the function definition in class)
    @staticmethod  -- > also known as decorator
    def fun():
        # some code

    if i don't use @staticmethod then it will show some error
        regarding use of self object
    
    Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,withoutpermanently modifying it
'''

class Manager:
    def __init__(self,name):
        self.name = name
    
    @staticmethod  # decorator
    def GreetingMessg():
        print("Hello world")


obj = Manager("Shailesh")
obj.GreetingMessg()
    

    
