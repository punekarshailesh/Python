'''
        Recursion - calling a function by itself repeatedly

        Base case - to stop the recursion

        memory ke andar  call stack for functions

        if base case is not written then recursion runs infinitely and at one point memory gets fulled and code crash
'''



def show(n):
    if n <= 0:
        return 
    print(n, end=" ")
    show(n-1)


show(5)
print()


def show(n):

    # base case
    if n <= 0:
        return
    show(n-1)
    print(n,end=" ")
    return

show(5)
print()

# Factorial

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n*fact(n-1)

print(fact(0 ))


# sum of first n natural numbers

def sum(n):
    if n == 0:
        return 0
    return n+sum(n-1)

print(sum(5))


# recursive function to print all elements in a list

def PRINT(List, ind):
    # base case
    if ind == len(List):
        return
    # process
    print(List[ind],end=" ")
    # recursive calle
    PRINT(List, ind+1)


PRINT([1,3,5,7,8],0)