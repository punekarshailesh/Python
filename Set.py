'''
        Set
            collection of unordered items
            each element in the set must be unique & immutable
            int, float, str, bool, tuples can be stored in sets
            no duplicate elements are stored/allowed

            Set - mutable hai but,
            Set -> elements -> immutable
'''



nums = {1, 3, 5, 4, 2, 2} # store 2 only one time
print(nums)


names = {"Shailesh", "Abhinay", "Shweta", "Yogesh", "Sakshi", 26, 25, 24, 21, 18,6.63,'Yogesh'}

print(type(names))

print(len(names))
# names.update("3892489r24")
# print(names)

# for items in names:
    # print(type(items))


# empty set

# null_set = {} # empty dictionary
null_set = set()  # emtpy set

print(type(null_set))


''' Methods of set '''

# set.add(arg) - add element
null_set.add(6.63)
null_set.add("Shailesh M")
null_set.add((1, 2, 3))
# null_set.add([33, 34, 35]) - Error as element of this list are mutable but elements of set are immutable
# null_set.add({1:"Math",2:"Science"}) - Error as dictionary is mutable

# null_set.add(nums) - Error unhashablle type set

print(null_set)

# set.remove(element) - removes the element

# null_set.remove(6.63)
# print(null_set)

# null_set.remove(6.6) # ERROR - key Error 


# set.clear() - empty the set
# null_set.clear()
# print(null_set)

# set.pop() - removes a random value
value = null_set.pop()
print(value)
print(null_set)


# set.union(another_sets) - combine 2 sets and return new set
set1 = {1, 2, 3, 5, 4,"Shailesh"}
set2 = {3, 5,"Shailesh", 4, 7}

set4 = set1.union(set2)
print("Union of 2 sets: ",set4)

# set.intersection(another_set) - common values and return new set


set3 = set1.intersection(set2)

print("Intersection of 2 sets: ",set3)

