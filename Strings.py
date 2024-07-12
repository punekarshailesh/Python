# string : sequence of characters

name1 = "Shailesh"
name2 = 'Shailesh Madne'
name3 = '''Shailesh maroti madne'''
str4 = """This is a string"""
print(name1)
print(name2)
print(name3)

# print(str1=("Shailesh B.Tech")) - ERORR


Str = ''' this is nitc's ''' 
print(Str)


''' 
    \n - new line character
    \t - tab space    
'''

name = '''this is shailesh. \tI am strating with the python'''
print(name)

# print(name,end=".")

'''
    Basic operations
'''

''' concatenation '''
str1 = "shailesh"
str2 = "madne"
print(str1+str2)

''' Length of string - len() '''
print(len(str1))
print(len(str2))
print("Length of the string: ",len(str1+ " "+ str2))


''' Indexing - like array starts index with 0 to len-1 '''
print(str1[0])
# str1[0] = 'S' -- ERROR because string object doesnot support item assignment/ at specific index position we cannot change the character
print(str1[7])


''' Slicing - Accessing parts of a string

    string[starting_index : ending_index] # ending index is not included

'''
Lapy = "Lenovo intel core"
print(Lapy[2:4]) # 2 to 4-1 i.e. 'no' from Lapy string
print(Lapy[:len(Lapy)]) # is same as the Lapy[0:len(Lapy)]
print(Lapy[1:]) # is same as the Lapy[1 : len(Lapy)]
# print(Lapy[:len(Lapy):4])
# print(Lapy[len(Lapy):]) -> empty string

'''
    Slicing using negative index end of the string starts with -1 and ends with -len(string)

              M   a   d  n  e
             -5  -4  -3 -2 -1  
'''

Str = "I am learning Slicing"

print(Str[-len(Str): ])
print(Str[-1 :  len(Str)])
print(Str[-3:])


# endswith() # True/False

print(Str.endswith("ing"))
print(Str.endswith("ge"))


# capitalize() # 1st character ko capital 

Str2 = "hello world"

print(Str2.capitalize()) # this will not change actual string

Str2 = Str2.capitalize() # this will change actual string as it stores in Str2
print(Str2)


# replace(old , new) - changes the occurrence of that character
print(Str2.replace("Hello","Welcome to"))


# find(arg)  - 1st index of 1st occurrence
print(Str2.find("world"))
print(Str2.find("Q")) # -1 invalid index return karega

# count(arg) - count the occurrence of the substring
Str3 = "Shailesh Maroti Madne. Shweta Madne. Sakshi Madne"

print(Str3.count('Madne'))

print(Str3.index("Madne"))