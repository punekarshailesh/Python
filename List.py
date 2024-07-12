'''
    Lists - A built in data type that stores set of values

    it can store elements of different type i.e. integer, float, string, etc..

*** Note
        -> strings are immutable(values cannot be changed at any index) in python but lists are mutable(values can be changed at any index) 

'''

marks = [94.4, 87.5, 95.2, 66.4, 40]
print(marks)
print(type(marks))
print(type(marks[1]))
print(len(marks))

# different types of data types elements can be stored in list
student_info = ["Shailesh maroti madne", 6.77, 'Pune','B.Tech']

print(student_info)
print(type(student_info))
print(type(student_info[0]))

student_info[0] = 'Shreyas S N'
print(student_info)


''' List slicing : list_name[start_index : end_index] '''

# print(student_info[1:2])
# print(student_info[:len(student_info)-1])
# print(student_info[0:])


# List slicing using -ve indexing

print(student_info[-4:])
print(student_info[:])
print(student_info[:-2])
print(student_info[-1:])


''' List methods '''

List = [3, 5.43, "APJ Kalam", "Former President"]


# append(arg) : add element at end of list -> return None
print(List.append("Scientist"))

print(List)

# list.sort() - sorting ascending order -> return None
# list.sort() - only works on the similar data type elements
# List.sort() - INVALID

# marks.sort()
# print(marks)

# list.sort(reverse=True) - sort in descending order
# marks.sort(reverse=True)
# print(marks)


# list.reverse() - reverses the list -> return None
# List.reverse()
print(List.reverse()) # Prints - None
print(List)

# list.insert(index, element) - insert element at given index -> return None
List.insert(0,"Age: 78")

print(List)

# list.remove(pass arg) - removes first occurence of that element
# List.remove("APJ") - ERROR because element is not present

num = [1, 2, 3, 1, 4, 3, 5, 3]
num.remove(1)
print(num)
# print(List)

''' list.pop(index)
        -> removes element at given index
'''
num.pop(3)
print(num)

print(num.count(3))


List = [(1,3,4),(4,5,6)]

for items in List:
    print(items)

for i in range(len(List)):
    print(List[i][2])

a = [1,2,3,1]
b = [1,2,3,1]

print(a==b)
print(a is b)
if a==b:
    print("valid")

import re
sentence = 'horses are fast'
regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
matched = re.search(regex, sentence)
print(matched.groups(2))
    