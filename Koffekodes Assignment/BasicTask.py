# Write a function to reverse a string without using slicing.

# def reversestring(string):
#     if string:
#         return reversestring(string[1:]) + string[0]
#     return string

# print(reversestring('Vishal'))


# Create a program to count the frequency of each character in a given string.

# def chfrequency(string):
#     result = {}
#     for char in string:
#         if char in result:
#             result[char] += 1
#         else:
#             result[char] = 1
#     return result

# print(chfrequency("Vishal"))


# Write a program to merge two dictionaries and add values of common keys.

# def mergdict(dict1,dict2):
#     if dict1 and dict2:
#         merge_dict = {**dict1, **dict2}
#         for key in dict1:
#             if key in dict2:
#                 merge_dict[key] = dict1[key] +dict2[key]
#         return merge_dict
#     elif dict1:
#         return dict1
#     elif dict2:
#         return dict2
#     else:
#         return{}
    
# print(mergdict({"name":"Vishal", "Subject":"Python"}, {"name":"rakshit", "Subject":"Java"}))


# Create a function to flatten a nested list.
# Example: [[1, 2], [3, [4, 5]]] -> [1, 2, 3, 4, 5]

# def nestedlist(nested_list):
#     lists = []
#     for i in nested_list:
#         if isinstance(i, list):
#             lists.extend(nestedlist(i))
#         else:
#             lists.append(i)
#     return lists

# print(nestedlist([[1, 2],0,0 ,[3, [4, 5, [6,7]]]]))


# Create a program to check if a given year is a leap year without using calendar.

# def leap_year(year):
#     if year % 4 == 0:
#         print("leap year")
#     else:
#        print("NOT leap year")    

# print(leap_year(2024))


# Implement a number guessing game where the program gives feedback (too high, too low).

# import random

# def guessing_game():
#     num = random.randint(1, 100)
#     while True:
#         guess = int(input("Guess number: "))
#         if guess == num:
#             print("Correct!")
#             break
#         elif guess < num:
#             print("Too low!")
#         else:
#             print("Too high!")

# guessing_game()


# Develop a program that finds the longest palindrome in a given string

# def palindrome(string):
#     string = ''.join(e for e in string if e.isalnum()).lower()
#     longest = ''
#     for i in range(len(string)):
#         for j in range(i + 1, len(string) + 1):
#             substring = string[i:j]
#             if substring == substring[::-1] and len(substring) > len(longest):
#                 longest = substring

#     return longest

# print(palindrome("yaaaaaay"))
# print(palindrome("nayan"))


# Write a function that takes a list and returns the second largest number.
    
# def largestnumber(lst):
#     if len(lst)<2:
#         return None
#     lst.sort(reverse = True)
#     return lst[1]

# print(largestnumber([25,3,21,27,5]))


# Implement a function to calculate the factorial of a number using recursion.

# def factorial(n):
    # if not isinstance(n, int):
    #     raise TypeError("Input must be an integer.")
    # if n < 0:
    #     raise ValueError("Input must be a non-negative integer.")
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))


# Create a program to find duplicates in a list without using sets.
# def find_duplicates(lst):
#     duplicates = []
#     for i in range(len(lst)):
#         if lst[i] in lst[i+1:] and lst[i] not in duplicates:
#             duplicates.append(lst[i])
#     return duplicates

# print(find_duplicates([1, 2, 3, 2, 4, 5, 5, 6]))


# Write a class that implements a basic calculator supporting add, subtract, multiply, and divide operations.
# class Calculator:
#     def addition(self, a, b=0):
#         return a + b

#     def multiply(self, a, b=1):
#         return a * b

#     def subtraction(self, a, b=0):
#         return a - b

#     def divide(self, a, b=1):
#         if b != 0:
#             return a / b
#         print ('Can not divide by zero')

# calculator = Calculator()
# print(calculator.addition(10))
# print(calculator.subtraction(50, 20))
# print(calculator.multiply(10, 20))
# print(calculator.divide(100, 20))


# Implement a class hierarchy for shapes (e.g., Circle, Rectangle) with area and perimeter methods.

# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return pi * self.radius ** 2

#     def perimeter(self):
#         return 2 * pi * self.radius

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# circle = Circle(5)
# print(f"Circle area: {circle.area()}, perimeter: {circle.perimeter()}")

# rectangle = Rectangle(4, 6)
# print(f"Rectangle area: {rectangle.area()}, perimeter: {rectangle.perimeter()}")


# Create a class for a bank account with deposit, withdraw, and check balance methods.
# class BankAccount:
#     def __init__(self, acc_holder,balance=0):
#         self.account_holder = acc_holder
#         self.__balance = balance
#     # Deposit mate
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"{amount} deposited successfully!")
#         else:
#             print("Invalid Amount!")
#     #withdraw mate
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"{amount} withdrawn successfully!")
#         else:
#             print("Insufficient Balance!")  

#     #Check bakance mate
#     def check_balance(self):
#         print(f"Available Balance: {self.__balance}")
    
# def main():
#     print("\n Banking System ")
#     name = input("Enter Account Holder Name: ")
#     account = BankAccount(name)

#     while True:
#         print("\n1. Deposit Money")
#         print("2. Withdraw Money")
#         print("3. Check Balance")
#         print("4. Exit")

#         choice = input("\nChoose an option (1/2/3/4): ")
        
#         if choice == '1':
#             amount = float(input("Enter Amount to Deposit: "))
#             account.deposit(amount)
        
#         elif choice == '2':
#             amount = float(input("Enter Amount to Withdraw: "))
#             account.withdraw(amount)
#             account.check_balance()

#         elif choice == '3':
#             account.check_balance()
        
#         elif choice == '4':
#             print("\nExited!")
#             break
        
#         else:
#             print("\nInvalid choice. try again.")

# main()


# Write a program to count the number of words in a file.
# def wordcount(filename):
#         with open(filename, 'r') as file:
#             text = file.read()
#             words = text.split()
#             return len(words)

# filename = input("Enter the filename: ")
# print("words:", wordcount(filename))


# Create a program to find and replace a word in a file with another word.

# def changeword(filename, old, new):
#     with open(filename, 'r') as file:
#         text = file.read()
#     with open(filename, 'w') as file:
#         file.write(text.replace(old, new))

# filename = input("Enter filename: ")
# old = input("old word: ")
# new = input("new word: ")
# changeword(filename, old, new)


# Implement a program to check if a file is empty.
# def emptyfile(filename):
#     with open(filename, 'r') as file:
#         text = file.read()
#         words = text.split()
#         if len(words) <= 0:
#             print("File is Empty") 
#         else:
#             print("Not empty")    
# filename= input("Enter the filename: ")
# emptyfile(filename)


# Write a script to sort a list of tuples based on the second element.

# def secondelement(tup):
#     return sorted(tup , key = lambda x: x[1])

# list = [(5,6),(1,2) , (3,4)]
# print(secondelement(list))


# Write a function to determine if two strings are anagrams of each other.

# def anagrams(s1, s2):
#     return sorted(s1) == sorted(s2)

# print(anagrams("vishal", "shalvi"))


# Create a function to find the GCD of two numbers without using built-in functions.

# def gcd(x,y):
#     while y:
#         x, y =y, x%y
#     return y
    
# print(gcd(55,25))
        

# Create a program to generate all permutations of a given string.

# from itertools import permutations

# def permutation(str):
#     pm = permutations(str)
#     for p in pm:
#         print(''.join(p))
# print(permutation("vishal"))        


# Implement a program to check if a string is a valid IP address.

# def ipaddres(ip):
#     str = ip.split(".")
#     if len(str) != 4:
#         return False
#     for part in str:
#         if not part.isdigit():
#             return False
#         if int(part) > 255 or int(part) < 0:
#             return False
#     return True

# ip = input("enter ip address: ")
# if ipaddres(ip):
#     print("valid ip address")
# else:
#     print("invalid ip address")


# Implement a function that calculates the sum of digits of a number until the sum is a single digit.

# def digit(num):
#     while num > 9:
#         num = sum(int(d) for d in str(num))
#     return num

# print(digit(2510))


# Write a decorator to time the execution of a function.

# import time
# from functools import wraps

# def time_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Function {func.__name__} executed in {execution_time} seconds")
#         return result
#     return wrapper

# @time_decorator
# def example_function():
#     time.sleep(2)
# example_function()
    

# Write a function to merge two files line by line into a third file.
# def mergefile(output1, output2, output_file):
#     with open(output1, 'r') as o1, open(output2, 'r') as o2, open(output_file, 'w') as fo:
#         for line1, line2 in zip(o1, o2):
#             fo.write(line1 + line2)
#         fo.write(o1.read())
#         fo.write(o2.read())

# mergefile('output1.txt','output2.txt','output3.txt')


# Create a script that reads a CSV file and prints it in a tabular format.

# from csv import DictWriter,DictReader
# with open('example.csv', 'w',newline='') as f:
#     dict_writer = DictWriter(f,fieldnames=['First_name','Lastname','Subject','age'])
#     dict_writer.writeheader()
#     dict_writer.writerow({
#         'First_name':'Vishal',
#         'Lastname': 'Sohaliya',
#         'age':22})
#     dict_writer.writerow({
#         'First_name':'Rakshit',
#         'Lastname': 'Dharaiya',
#         'age':23})

# with open('example.csv', 'r') as rf:
#     with open('write_csv.csv', 'w') as wf:
#         csv_reader = DictReader(rf)
#         csv_writer = DictWriter(wf,fieldnames=['First_name','Lastname','age'])
#         csv_writer.writeheader()
#         for row in csv_reader:
#             First_name, Lastname, age = row['First_name'],row['Lastname'], row['age']
#             csv_writer.writerow({
#                 'First_name': First_name,
#                 'Lastname': Lastname,
#                 'age': age,
#             })
        

# Write a program to find all prime numbers in a given range.

# start = int(input("Enter the starting range: "))
# end = int(input("Enter the ending range: "))
# for i in range(start, end+1):
#     flag = 0
#     for j in range(2, i):
#         if (i % j == 0):
#             flag = 1
#             break
#     if (flag == 0):
#         print(i, end=' ')        


# Implement a function to check if a number is an Armstrong number.

# i  = int(input("Enter a number to chack for armstrong: "))
# orig = i
# sum = 0

# while (i > 0):
#     sum = sum +(i%10)*(i%10)*(i%10)
#     i=i//10
# if orig == sum:
#     print("Number is Armstrong")
# else:
#     print("Numbe is not armstrong")        


#Create a class for a queue using lists with methods for enqueue, dequeue, and checking if empty.

# from collections import deque

# dq = deque([10,20,30])
# dq.appendleft(5)
# dq.pop()
# print(dq)

############################################

# class Queue():
#     def __init__(self, items=None):
#         self.queuelist = items if items is not None else []

#     def enqueue(self, item):
#         self.queuelist.append(item) # add element

#     def is_empty(self):
#         return len(self.queuelist) == 0

#     def dequeue(self): 
#         if not self.is_empty():
#             return self.queuelist.pop(0) # 0 index thi remove
#         else:
#             return None 
        
# o1 = Queue()
# o1.enqueue(10)
# o1.enqueue(10)        
# o1.enqueue(10) 
# o1.is_empty
# print(o1)       


# Write a program to generate Pascal's triangle up to a given number of rows.

def print_row_1(): # row 1
    print("1", end="")

def print_row_2(): # row 2
    print("1 1", end="")  

def print_row(row):
    for i in row:
        print(i, end=" ")

def print_pascal_triangle(n):
    previous_row = [1,1]
    for i in range(1,n+1):
        if (i == 1): # print 1st row
            print_row_1()
        elif(i == 2): #print second row
            print_row_2()
        else:
            row = [0 for j in range(i)] 
          # first and last element 1 print karvane ke liye.
            row[0] = 1
            row[i-1] = 1
        
            for  j in range(1, i-1): # upar na digits no sum karva mate
                row[j] = previous_row[j] + previous_row[j-1]
            print_row(row)
            previous_row=row    
        print()     

n = 8
print(print_pascal_triangle(n))        


# Write a class to represent a 2D point and implement methods for calculating distance from another point.

# import math

# class calculating_distance_another_point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def calculate_distance(self, other_point):
#         dis_x = self.x - other_point.x
#         dis_y = self.y - other_point.y

#         return math.sqrt(dis_x**2 + dis_y**2)

# o1 = calculating_distance_another_point(2, 9)
# o2 = calculating_distance_another_point(13, 24)

# print(o1.calculate_distance(o2))  
# print(o1)

                                                
                 
        

        