#list_name.extend(iterable)

#Example:
# list_2 = [1, 2, 3]

# list_2.extend((4,5,6))

# print(list_2)

# statesAndCapitals = {
#     'Gujarat': 'Gandhinagar',
#     'Maharashtra': 'Mumbai',
#     'Rajasthan': 'Jaipur',
#     'Bihar': 'Patna'
# }
# map_keys = map(statesAndCapitals.get, statesAndCapitals)
# for values in map_keys:
#     print(values)

# statesAndCapitals = {
#     'Gujarat': 'Gandhinagar',
#     'Maharashtra': 'Mumbai',
#     'Rajasthan': 'Jaipur',
#     'Bihar': 'Patna'
# }
# for state, capital in zip(statesAndCapitals.keys(), statesAndCapitals.values()):
#     print(f'The capital of {state} is {capital}')

# import asyncio

# async def Transection():
#     print("Please wait for 6-7 seconds")
#     await asyncio.sleep(6)
#     print("Collect your cash")
#     await asyncio.sleep(3)
#     print("transection Successsfull")

# asyncio.run(Transection())   

# import asyncio

# async def task1():
#     await asyncio.sleep(2)
#     print("Task 1 complete")

# async def task2():
#     await asyncio.sleep(2)
#     print("Task 2 complete")

# async def main():
#     await asyncio.gather(task1(), task2())  

# asyncio.run(main())

# def log_and_validate(method):
#     def wrapper(self, *args, **kwargs):
#         print(f"Calling {method.__name__}")

#         ## Input validation
#         for arg in args:
#             if not isinstance(arg, (int, float)):
#                 raise TypeError("Arguments must be numeric")

#         result = method(self, *args, **kwargs)

#         print(f"{method.__name__} completed successfully")
#         return result
#     return wrapper

# class Calculator:
#     @log_and_validate
#     def divide(self, a, b):
#         return a / b

# Tuples
# Write a Python program to:

# Create a tuple with 5 elements.
# Access the 3rd element and print it.
# a = (1,2,3,4,5)
# print(a[2])

# Convert the tuple into a list, modify the 2nd element, and convert it back to a tuple.
# a = (1,2,3,4,5)
# b = list(a)
# b[2] = 55
# a=tuple(b)
# print(a)


# Given a tuple data = (10, 20, 30, 40, 50):

# Unpack the tuple into individual variables.
# tupledata=(10,20,30,40,50)
# a,b,c,d,e= tupledata
# print(tupledata)
# print(a,b,c,d,e)

# # Find the index of the value 30.
# print(tupledata.index(30))
# # Check if the value 60 exists in the tuple.
# print(60 in tupledata)

# # Create a tuple of numbers and write a program to:
# tupledata=(10,20,30,30,40,40,50)
# # Find the maximum and minimum values in the tuple.
# print(max(tupledata))
# print(min(tupledata))
# # Count the occurrences of a specific number in the tuple.
# print(tupledata.count(30))    
# # Sets
# # Write nion, intersection, and difference of the sets.
# # Check if A is a subseta Python program to:

# # Create two sets: A = {1, 2, 3, 4} and B = {3, 4, 5, 6}.
# A ={1,2,3,4}
# B={3,4,5,6}
# # Find the u of B.
# print('u' in B)

# # Given a list of numbers with duplicates, write a program to:
# listdata=[1,2,2,3,3,4,4,5,5,6,2,1,5,2]
# # Convert the list into a set to remove duplicates.
# setdata = set(listdata)
# print(setdata)
# # Add a new number to the set.
# setdata.add(100)
# # Print the updated set.
# print(setdata)
# # Create a program that:
# student1= "vishal"
# student2= "Rakshit"

########################################################################################################################################

# Takes two sets of student names.#list_name.extend(iterable)

#Example:
# list_2 = [1, 2, 3]

# list_2.extend((4,5,6))

# print(list_2)

# statesAndCapitals = {
#     'Gujarat': 'Gandhinagar',
#     'Maharashtra': 'Mumbai',
#     'Rajasthan': 'Jaipur',
#     'Bihar': 'Patna'
# }
# map_keys = map(statesAndCapitals.get, statesAndCapitals)
# for values in map_keys:
#     print(values)

# statesAndCapitals = {
#     'Gujarat': 'Gandhinagar',
#     'Maharashtra': 'Mumbai',
#     'Rajasthan': 'Jaipur',
#     'Bihar': 'Patna'
# }
# for state, capital in zip(statesAndCapitals.keys(), statesAndCapitals.values()):
#     print(f'The capital of {state} is {capital}')

# import asyncio

# async def Transection():
#     print("Please wait for 6-7 seconds")
#     await asyncio.sleep(6)
#     print("Collect your cash")
#     await asyncio.sleep(3)
#     print("transection Successsfull")

# asyncio.run(Transection())   

# import asyncio

# async def task1():
#     await asyncio.sleep(2)
#     print("Task 1 complete")

# async def task2():
#     await asyncio.sleep(2)
#     print("Task 2 complete")

# async def main():
#     await asyncio.gather(task1(), task2())  

# asyncio.run(main())

# def log_and_validate(method):
#     def wrapper(self, *args, **kwargs):
#         print(f"Calling {method.__name__}")

#         ## Input validation
#         for arg in args:
#             if not isinstance(arg, (int, float)):
#                 raise TypeError("Arguments must be numeric")

#         result = method(self, *args, **kwargs)

#         print(f"{method.__name__} completed successfully")
#         return result
#     return wrapper

# class Calculator:
#     @log_and_validate
#     def divide(self, a, b):
#         return a / b

# Tuples
# Write a Python program to:

# Create a tuple with 5 elements.
# Access the 3rd element and print it.
# a = (1,2,3,4,5)
# print(a[2])

# Convert the tuple into a list, modify the 2nd element, and convert it back to a tuple.
# a = (1,2,3,4,5)
# b = list(a)
# b[2] = 55
# a=tuple(b)
# print(a)


# Given a tuple data = (10, 20, 30, 40, 50):

# Unpack the tuple into individual variables.
# tupledata=(10,20,30,40,50)
# a,b,c,d,e= tupledata
# print("Tuple data:", tupledata)
# print("Unpacked variables:", a,b,c,d,e)

# Find the index of the value 30.
# print("Index of 30:", tupledata.index(30))
# Check if the value 60 exists in the tuple.
#print("Is 60 in tupledata?", 60 in tupledata)

# Create a tuple of numbers and write a program to:
#tupledata=(10,20,30,30,40,40,50)
# Find the maximum and minimum values in the tuple.
# print("Maximum value:", max(tupledata))
# print("Minimum value:", min(tupledata))
# Count the occurrences of a specific number in the tuple.
#print("Count of 30:", tupledata.count(30))    
# Sets
# Write nion, intersection, and difference of the sets.
# Check if A is a subseta Python program to:

# Create two sets: A = {1, 2, 3, 4} and B = {3, 4, 5, 6}.
# A ={1,2,3,4}
# B={3,4,5,6}
# Find the u of B.
#print('Is "u" in B?', 'u' in B)

# Given a list of numbers with duplicates, write a program to:
# listdata=[1,2,2,3,3,4,4,5,5,6,2,1,5,2]
# Convert the list into a set to remove duplicates.
# setdata = set(listdata)
# print("Set data:", setdata)
# Add a new number to the set.
#setdata.add(100)
# Print the updated set.
#print("Updated set:", setdata)
# Create a program that:
# student1= input("Enter name: ")
# student2= input("Enter name: ")

# # Takes two sets of student names.
# # Finds the names that are common in both sets.
# # Finds the names that are unique to each set.
# student1_set = {student1}
# student2_set = {student2}
# # Finds the names that are common in both sets.
# print("Common names:", student1_set.intersection(student2_set))
# # Finds the names that are unique to each set.
# print("Unique names in student1:", student1_set.difference(student2_set))
# print("Unique names in student2:", student2_set.difference(student1_set)) 

#recursion, oops, inheritence, functions, use of __init__.py file,


# thisset = {"apple", "banana", "cherry"}
# # tropical = {"pineapple", "mango", "papaya"}
# # set3 = thisset.discard("Cherry")
# # # thisset.update(tropical)
# thisset.discard("apple")
# print(thisset)

#####################################################

# Exercise 1: Basic Set Operations
# Write a Python program to:

# Create two sets: set1 = {1, 2, 3, 4, 5} and set2 = {4, 5, 6, 7, 8}.

# set1 = {1, 2, 3, 4, 5} 
# set2 = {4, 5, 6, 7, 8}

# Perform the following operations:
# Find the union of set1 and set2.
# set3= set1.union(set2)
# print(set3)

# Find the intersection of set1 and set2.
# set4= set1.intersection(set2)
# print(set4)

# Find the difference between set1 and set2 (elements in set1 but not in set2).
# set5= set1.difference(set2)
# print(5)

# Find the symmetric difference between set1 and set2.
# set6= set1.symmetric_difference(set2)
# print(set6)

# Returns the list of unique elements sorted in ascending order.
# remove_duplicates_input = input("Add integers: ")
# print(sorted(list(set(remove_duplicates_input))))
# Example:
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

# Exercise 3: Set Membership
# Write a Python program to:
# Create a set of fruits: fruits = {"apple", "banana", "cherry", "date"}.
# fruits= {"apple", "kiwi","banana","graps"}
# Check if the following items are in the set:
# "apple"
# "grape"
# print("banana" in fruits)

# Add "anjeer" to the set if it is not already present.
# fruits.add("anjeer")
# print(fruits)

# Remove "banana" from the set if it exists.
# fruits.remove("banana")
# print(fruits)

# class Mobile:
#     def __init__(self,m):
#         self.model = m
# realme = Mobile('Realme X') 

# class Mobile:
#     def __init__(self):
#         self.model = 'Realme10'
#         print('This is constructor, Called only class')
#     def show_model(self):
#         print("Model:",self.model)   

# realme = Mobile()
# realme.show_model()

# class Myclass:
#     def __init__(self,value):
#         self._value = value
#     def show(self):
#         print(f"Value is {self._value}")
#     @property    
#     def ten_value(self):
#         return 10* self._value
# obj = Myclass(10)
# print(obj.ten_value)
# obj.show()  


# Accessing Private Members Using Name Mangling
# class Secret:
#     def __init__(self):
#         self.__hidden_value = 42  # Private attribute

# Creating an object
# secret_obj = Secret()

# Accessing private attribute using name mangling
# print("Accessing private attribute:", secret_obj._Secret__hidden_value)  
#                                     obj_name  class_name  Private_atrib_name

#Abstract method
# from abc import ABC, abstractmethod

# class Car():
#     def show(self):
#         print("Every car has 4 wheeler")

#     @abstractmethod
#     def speed(self):
#         pass    

# class Maruti(Car):
#     def speed(self):
#         print("Speed is 100 km/hr")

# class Suzuki(Car):
#     def speed(self):
#         print("Speed is 70Km/hr")

# obj = Maruti()
# obj.show()
# obj.speed()

# obj2 = Suzuki()
# obj2.show()
# obj2.speed()

# Python object serializers

#wb means Write Binary
#rb means Read binary
# import pickle

# # Define a dictionary to serialize
# data = {"name": "Arjun", "age": 25, "city": "New York"}

# # Serialize and save to file
# with open("data.pkl", "wb") as file:
#     pickle.dump(data, file)

# # Deserialize and load from file
# with open("data.pkl", "rb") as file:
#     loaded_data = pickle.load(file)

# # Print the loaded data
# print("Deserialized Data:", loaded_data)

# import pickle

# cars = ["Audi", "BMW", "Maruti", "Suzuki"]

# file = "car.pkl"
# fileobj= open(file,'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

# file= "car.pkl"
# fileobj = open(file,'rb')
# mycar = pickle.load(fileobj)
# print(mycar) 


# list1= ["a", "b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
# sublist=["h","i","j"]
# list1[2][1][2].extend(sublist)
# print(list1)
# Output = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

# a = 10
# b= 20

# a,b = b,a

# print(a)
# print(b)

# list1= ["hello", "python"]
# list2= ["world","react"]
# list3 = [x+y for x in list1 for y in list2]
# print(list3)

# def merge_tuple(tuple1, tuple2):
#     combined = []
#     for item in tuple1:
#         if item not in combined:
#             combined.append(item)
#     for item in tuple2:
#         if item not in combined:
#             combined.append(item)
#     return tuple(combined)

# tuple1 = (1, 2, 3, 4, 5, 6, 7)
# tuple2 = (4, 5, 6, 7, 8, 9, 10)
# combined_tuple = merge_tuple(tuple1, tuple2)
# print("Combined Tuple (without duplicates):", combined_tuple)


# def tuplelist(names, ages):
#     paired = []
#     for i in range(len(names)):
#         paired.append((names[i], ages[i]))
#     return paired

# names = ('vishal', 'rakshit', 'viraj')
# ages = (22, 23, 26)
# name_age = tuplelist(names, ages)
# print("Name-Age List:", name_age)


# nested_student_dict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# nested_student_dict["class"]["student"]["name"] = "jay"
# print(nested_student_dict)

#print same values in diffrent keys
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# pairs=  dict.fromkeys(employees,defaults)  
# print(pairs)

# get name and salary only
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# keys = ["name", "salary"]
# new_dict = {k: sample_dict[k] for k in keys}
# print(new_dict)


#remove name and salary
# dicts = {
#     "name": "jay",
#     "age" : 21,
#     "salary": 5200,
#     "city": "Surat" 
# } 
# keys = ["name", "salary"] 

# for key in keys:
#     dicts.pop(key)
# print(dicts)    

# output = {'age': 21, 'city': 'Surat'}                                            

# checks if values exists in ?
# dicts = {
#     "name" : "jay",
#     "age" : 21,
#     "salary" : 5200,
#     "City": "Surat"
# }

# if 5200 in dicts.values():
#     print("value exist")
# else: 
#     print("value dosen't exist")    

# change the Key
# dicts = {
#     "name" : "jay",
#     "age" : 21,
#     "salary" : 5200,
#     "City": "Surat"
# }
# dicts["Location"] = dicts.pop("City")
# print(dicts)

# dicts = {
#     "name" : "jay",
#     "age" : 21,
#     "salary" : 5200,
#     "City": "Surat"
# }
# dicts = {
#     "name" : "jay",
#     "age" : 21,
#     "salary" : 5200,
#     "City": "Surat"
# }# dicts = {
#     "name" : "jay",
#     "age" : 21,
#     "salary" : 5200,
#     "City": "Surat"
# }


# change value of key
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6000}
# }

# sample_dict["emp1"]["salary"] = 8500
# print(sample_dict)

# original_dicts = {"a": 1, "b":2, "c":3}
# swapped_dict = {values:key for key, values in original_dicts.items()}
# print(swapped_dict)

# HCF LCM
# def find_hcf(a,b):
#     while b:
#         a,b = b , a%b
#     return a

# a =48
# b =18

# hcf = find_hcf(a,b)
# lcm = (a*b) // hcf 

# print("HCM ",hcf)    
# print("LCM ",lcm)  


# c= float(int(input("Enter temperature in celcious ")))
# f = (c * 9/5) + 32

# print(f"{c}°C is equal to {f:.2f}°F")

# f = float(int(input("Enter temperature in fahrenhit: ")))
# c = (f-32) * 5/9
# print(f"{f:.2f}°F is equal to {c}°C")


# nested for loop
# employees = [("Dorothy", "DevOps"), ("Abdel", "HR"), ("Nataliya", "DevOps")]
# departments = [
#     {"name": "DevOps", "city": "Berlin"},
#     {"name": "HR", "city": "Abuja"},
# ]

# for name, department in employees:
#     for dept in departments:
#         if dept["name"] == department:
#             print(f"{name} works in {dept['city']}")


# resource_donetors = [
#     [6, 2, 7],
#     [9, 3, 5],
#     [4, 1, 8]
# ]       

# total_resources = 0
# for planet in resource_donetors:
#     for resource in planet:
#         total_resources += resource
# print("Answer",total_resources)

# resource_vs = ["vishal", "viraj","rakshit","akash"]

# for i in resource_vs:
#     for y in resource_vs:
#         print(f"{i} vs {y}") 

# num = "Hello"
# results = isinstance(num, int)

# if results:
#     print("yes")
# else:
#     print("No")

# main_list = ['Emma', 'Stevan', 12, 45.6, 1 + 2j, "Eric", ]
# sub_list1 = []
# sub_list2 = []

# for item in main_list:
#     if isinstance(item,(int,float,complex)):
#         sub_list1.append(item)
#     elif isinstance(item,str):
#         sub_list2.append(item)
        
# print(sub_list1)
# print(sub_list2)

# even_num = 5
# if even_num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# str = "My salary is 7000"
# print(str.isalnum())

# set_ex = {1,"orange", "blue"}
# for orange in set_ex:
#     print(orange)
