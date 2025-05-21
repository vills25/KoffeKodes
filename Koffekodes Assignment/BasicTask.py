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
       

# Write a program to find all prime numbers in a given range.



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