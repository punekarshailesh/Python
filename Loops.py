'''
        While

        while condition:
            # code 


'''

i = 0  # i called as iterator
while i<5:
    print("hello",i)  # iteration
    i +=1



'''     Break statement - to terminate the loop    '''

i = 1
while i<20:
    if i%7 == 0:
        break
    print(i)
    i+=1


'''     Continue statement - skip the iteration and continue to next iteration  '''
i = 1
while i<=20:
    if i == 5:
        i += 2
        continue
    print(i)
    i += 1

# printing odd using continue statement

i = 1
while i<10:
    if i%2 == 0:
        i+=1
        continue
    print("Odd numbers are: ",i)
    i +=1 

# printing even numbers
i = 1
while i<=10:
    if i%2 != 0:
        i+= 1
        continue
    print("Even numbers are: ",i)
    i += 1


'''     
        for loops
            -> sequential traversal
'''

List = [1, 3, "shailesh"]

for items in List:
    print(items)

# FOR LOOP WITH ELSE , else is optional

for items in List:
    if items%3 == 0:
        break
    print(items)    
else:
    print("Loop ended")


print()
# range(start, stop, step)

for i in range(5): # range(stop)
    print(i)      # 0, 1, 2, 3, 4
print(range(5))
for i in range(1, 5): # range(start,stop)
    print(i)      # 1, 2, 3, 4

print("Odd numbers: ")
for i in range(1, 10, 2): # range(start, stop, skip)
    print(i)      # 1, 3


print("Even numbers: ")
for i in range(2, 10, 2):
    print(i)


'''     pass statement  - is a null statement that does nothing. It is used as a placeholder for future code    '''

for i in range(10):
    # empty
    pass
# if i just keep a loop as it is it willnot execute the next part of that loops so we need pass statement
print("Some useful work!") 