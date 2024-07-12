'''
        Tuples

        * A built-in data type that let us create immutable sequences of values
        * can different data types elements i.e. string, float, int, etc..
        * once made cannot insert values, delete values, etc
''' 

Tup = (87, 64, 33, 95, 76)

print(Tup)
# Tup[0] = 83 - Immutable so cannot change values

friends_name = ("Shreyash Salunke",22, "Prathmesh W", 23)

print(friends_name)
print(friends_name[2])


# Different types for creating tuples
tup = ()
tup1 = (23) # -> integer value
tup2 = (1,)
tup3 = (3, 5, 43)

print(type(tup), "\n",type(tup2), "\n", type(tup3), "\n",type(tup1))


''' Slicing '''

print(friends_name[:2])
print(friends_name[:])

print(friends_name[-4:])


''' Methods '''

# tup.count(val) - returns number of occurences
print(Tup.count(83))

# tup.index(val) - returns the index of the value
print(friends_name.index(22))