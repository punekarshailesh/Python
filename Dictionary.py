'''
        Dictionary:
            Store data values in key:value pairs

            unordered, mutable(changable) and don't allow duplicate keys

            Dict[key] = value

            *key can be string, int, float, tuple. The values which cannot be changed once it is assigned
            *value can be anything - int, float, tuple, list, dictionary, etc...

'''


# Dict = {
#     "name" : "Shailesh",
#     "cgpa" : 6.77,
#      "marks":[52, 55, 64, 89] ,# key : list
#      "Is_pass":True,
#      "Subjectvise_marks":{"Coding theory":30.5,"Sanskrit":45, "NLP":65, "ProjectII":82} ,    # key : dictionary - also known as nested dictionary
#      12.44 : 38,
#      "info":("B200849CS","") # key : tuple
# }


# print(Dict)
# print(type(Dict))

# print(Dict["name"])

# # accesing key with dictionary as their value
# print(Dict["Is_pass"])

# # accessing nested dictionary values
# print(Dict["Subjectvise_marks"]["Coding theory"]) 

# # accessing key with list as their value
# print(Dict["marks"][2])


# # changing/updating the values
# Dict["name"] = "Shailesh Maroti Madne" # overwrite

# Dict["Subjectvise_marks"]["Coding theory"] = Dict["Subjectvise_marks"]["Coding theory"] + 5

# print(type(Dict["marks"]))

# # adding new values in dictionary
# Dict["info"] = ("B200849CS","F-hostel",211)
# print(Dict)
# print(Dict.keys())


# # null dictionary
# null_dict = {}


# print(null_dict)


# Nested dictionary



college_info = {
    1:{
        "name" : "Shailesh M",
        "Roll No": "B200849CS",
        "Sem" : 7,
        "Coursework": {
            "Manjusha":{
                "Data Mining" : 'D',
                "Software Engineering" : 'C'
            },
            "Pournami P N":{
                "Machine Learning Lab":'B'
            },
            "Raju Hazari":{
                "TOC":'D',
                "Coding theory":'E',
                "ProjectI":'B'
            },
            "Pranesh Das":{
                "Subjects":{
                    "DBMS":6,
                    "DBMS Lab":6,
                    "ProjectI":7,
                    "ProjectII":8
                },
                "Grade":{
                     "DBMS":'D',
                    "DBMS Lab":'B',
                    "ProjectI":'B',
                    "ProjectII":'A'
                }
            },
            "Amit Praseed":{
                "ProjectI":'B',
                "ProjectII":'A'
            },
            "Paleri":{
                "Compiler Design":'E'
            }
        },
        

    }

}


# Accessing values
print("College Info: ",college_info[1])
print()
print("Sem: ",college_info[1]["Sem"])
print()
print("Coursework: ",college_info[1]["Coursework"])
print()
print("Teacher: ",college_info[1]["Coursework"]["Pranesh Das"])
print()
print("Teacher Taught subjects with sem: ",college_info[1]["Coursework"]["Pranesh Das"]["Subjects"])
print()
print("Grade: ",college_info[1]["Coursework"]["Pranesh Das"]["Grade"]["ProjectII"])
print()


''' Dict Methods '''

# Typecasting
# print(list(college_info[1]['Coursework'].keys()))

# print(college_info.values())


# dict.items()
# print(college_info.items())
# print(type(college_info.items()))

# List = list(college_info.items()) # typecasting dictionary -> list

# print(type(List[0])) # tuple

''' dict.get("key") '''
print(college_info.get(1))

# print(college_info[2]) # key error
print(college_info.get(2)) # simply return None


'''     dict.update(new_dict)   
            either dictionary/{key:value} as a arg
'''
college_info.update({2:{}})

print(college_info)