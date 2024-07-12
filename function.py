'''
    functions

        block of statements that performs specific task

        def function_name(parameter1, param2, .....):
        # some code/work
        return something/nothing

        *reduced number of lines of code
        *reduces redundancy

'''
# user defined functions

# a and b are parameters
def sum(a , b):
    return a + b



value = sum(a=int(input()), b=int(input()))   # function call and a,b are arguments
print(value)


# the function where no return value is there it returns None
def print_hello():
    print("Hello world")

output = print_hello()  # return None value
print(output)

# cal average of 3 num
def avg(a , b, c):
    return (a+b+c)/3

print(avg(3, 4, 5))
print(round(avg(4, 5, 8),3),int(avg(4, 5, 8)))

# built-in functions
print("Shailesh",end=" ")
print("Madne")

print(type("Shailesh"))

''' 
        Default parameters
         -> default values are taken when there are no arguments passed at the time of function call
         -> but if values are passed as argument in function call then that values are taken not the default values

'''



def prod(a=4 , b=5):
    return a*b

print(prod(6,6))


# def prod(a=4,b): - throw an error as non default argument shouldnot come last i.e. first default value should be present in b then a 
# passing value in default argument is from right to left
 


