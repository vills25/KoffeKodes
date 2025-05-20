#Calculate the factorial of a number using recursion.
# def factorial(n):
#     if n < 0:
#         print("Input must be a non-negative integer.")
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# n = 5  
# print(f"The factorial of {n} is: {factorial(n)}")


# Calculate the sum of all elements in a list using recursion.
# def sum_of_list(lst):
#     if not lst:
#         return 0
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_of_list(lst[1:])

# lst = [1,2,3,4,5,6]
# result = sum_of_list(lst)
# print(f"The list sum is {result}")


# Write a function that checks if a given string is a palindrome (reads the same forwards and backward), ignoring spaces and letter casing.
# def palindrome(s):
#     s = ''.join(c for c in s if c.isalnum()).lower()
#     if s == s[::-1]:
#         print("String is palindrome")
#     else:
#         print("String is NOT-palindrome")

# s = 'nAyan'
# palindrome(s)


# Count the number of elements in a list using recursion.
# def count_elements(lst):
#     if not lst:
#         return 0
#     else:
#         return 1 + count_elements(lst[1:])

# lst = [1, 2, 3, 4, 5, 6]
# result = count_elements(lst)
# print(f"number of elements in the list: {result}")


# Implement a function that calculates the sum of the digits of a positive integer.
# def sum_of_digits(n):
#     if not isinstance(n, (int, list, tuple)) or any(not isinstance(i, int) or i <= 0 for i in n):
#         return("invalid input")
#     if isinstance(n, (list, tuple)):
#         return sum(sum(int(digit) for digit in str(i)) for i in n)
#     else:
#         return sum(int(digit) for digit in str(n))
 
# n = 1,2,3,5,6,4
# print(f"The sum of digits is: {sum_of_digits(n)}")


# Write a program that performs operations on lists, such as finding the maximum element, sorting, and removing duplicates.
# def lists(lst):
#     # Find maximum element
#     max_element = max(lst)
#     print(f"maximum element: {max_element}")

#     # Sort list
#     sorted_list = sorted(lst)
#     print(f"sorted list: {sorted_list}")

#     # Remove duplicates
#     unique_list = list(set(lst))
#     print(f"list with no duplicates: {unique_list}")

# lst = [5, 2, 8, 1, 4, 2, 5, 9]
# lists(lst)


# Implement a function that checks if a given year is a leap year.
# def leap_year(year):
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         print("leap year")
#     else:
#        print(f"{year} is NOT leap year")    
# year = 2025
# print(leap_year(year))


# Implement the FizzBuzz game: Print numbers from 1 to n, but for multiples of 3, print "Fizz," for multiples of 5, print "Buzz," and for multiples of both 3 and 5, print "FizzBuzz."
# def fizzbuzzgame(n):
#     result= []
#     for i in range(1, 1+n):
#         if i % 3 == 0 and i % 5 == 0:
#             result.append("Fizzbuzz")
#         elif i % 3 == 0:
#             result.append("Fizz")
#         elif i % 5 == 0:
#             result.append("Buzz")  
#         else:
#             result.append(str(i)) 
#     return result

# n = 20
# print(' '.join(fizzbuzzgame(n)))      
              
                 
# Create a simple number guessing game where the program generates a random number, and the user has to guess it.
# import random

# def guessing_game():
#     generatednum = random.randint(1, 100)
#     n = int(input("Guess a number: "))
    
#     if n == generatednum:
#         print("Correct", generatednum)
#     else:
#         print("Incorrect.", generatednum)

# guessing_game()

        