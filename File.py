''' 
        File I/O
         perform operations in file (read and write)

         Types of files:
                Text : .txt, .docx, .log etc..
                Binary Files : .mp4, .mov, .png, .jpeg etc...


         RAM - volatile memory i.e. once system is closed created data/variables are permanently deleted

         
        f = open("file_name", "mode")
        file_name - file.txt, demo.docx, .mp4
        modes:
                r : read mode (default)
                w : open for writing, truncating the file first(overwrite the data which is already present in the file )
                x : create a new file and open it for writing
                a : open for writing, appending to the end of the file if it exists
                b : binary mode
                t : text mode(default mode hota hai)
                + : open a disk file for updating (reading and writing)
                r+ : for both reading and writing. data not truncated
                w+ : for both reading and overwriting the present data. data truncated(i.e. data is not printed)
                a+ : reading and appending. data not truncated
        file_name if it present somewhere else then we have to write the path of the file

        In mode: w/a if file is not present then it will automatically create a new file

'''



f= open("demo.txt","r")

data = f.read()
print(data)
print(type(data))
f.close()  # closing the file is important

f2 = open("xyz.txt","r")

# f2.write("Lets begin our journey in Gramener!")

data = f2.read()
print(data)
f2.close()

# a - used for writing, appending to the end of the file if it exists

f2 = open("xyz.txt","a")

f2.write("\tAdded at the end of the file")

f2.close()

f2 = open("xyz.txt","r")
data = f2.read()
print(data)

f2.close()




# to read file line by line
f2 = open("demo.txt","r")

line1 = f2.readline()
print(line1)

line2 = f2.readline()
print(line2)

line3 = f2.readline()
print(line3)

line4 = f2.readline()
print(line4)

f2.close()

f3 = open("demo.txt","r+")
f3.write("Hello shailesh") # complete overwrite nahi karta start ka part of the file overwrite karega
print(f3.read())
f3.close()


f4 = open("demo.txt","w+")
f4.write("Lets overwrite everything in this demo.txt file!")
print(f4.read()) # as files content is deleted when we open w+ mode so no data is printed only the empty line is printed
f4.close()


# with Syntax

with open('demo.txt','w') as f:
    data = f.write("Let's understand the python file correctly!")
    print(data)
# f.close() no need to close the file when with syntax as it automatically closes the file


with open("demo.txt","w") as f:
    f.write("New Data")
    



'''     Deleting a File     
            using the modules
'''



