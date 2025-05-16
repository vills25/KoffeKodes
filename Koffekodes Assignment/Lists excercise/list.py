# Given a list of numbers, write a function that takes the list as input and returns a new list containing only the even numbers from the original list.

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
even_numbers = [num for num in num_list if num % 2 == 0]
print(even_numbers)

# Create a list of names and then write code to sort the list alphabetically in descending order.

name = ["vishal", "rakshit", "viraj", "darshan", "koffekodes"]
name.sort(reverse=True)
print(name)

#Create a list of numbers from 1 to 10 and then use a list comprehension to create a new list containing the squares of these numbers.

list = list(range(1,11))
squares= [num ** 2 for num in list]
print(squares)

# Write a function that takes two lists as input and returns a new list containing elements that are common to both input lists (intersection).

def intersection(list1, list2):
    return[element for element in list1 if element in list2]

list1=[1,2,3,4,5,6,7,8]
list2=[5,6,7,8,9,10]
print(intersection(list1,list2))

# Write a function that takes a list as input and returns a new list with the elements reversed, without using the built-in reverse method.

def reversedele(elementslist):
    return elementslist[::-1]
elementslist = [1,2,3,4,5,6,7,8,9]
print(reversedele(elementslist))

# Write a function that takes two lists as input and returns a new list that contains the elements that are unique to each list (i.e., not common to both lists).
def unique_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 ^ set2)

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [5, 6, 7, 8, 9, 10]
print(unique_elements(list1, list2))


