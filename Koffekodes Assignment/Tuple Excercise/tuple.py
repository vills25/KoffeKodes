# Create a function that takes three arguments (name, age, city) and returns them as a tuple. Then, call the function and unpack the tuple into separate variables.
    
def create_pack(name, age, city):
    return (name, age, city)

pack = create_pack('Vishal', 22, 'Surat')
name, age, city = pack
print(pack)

# Given two tuples, create a new tuple that combines elements from both tuples without any duplicates.

def merge_tuple(tuple1, tuple2):
    return tuple(set(tuple1 + tuple2))

tuple1 = (1, 2, 3, 4, 5, 6, 7)
tuple2 = (4, 5, 6, 7, 8, 9, 10)
combined_tuple = merge_tuple(tuple1, tuple2)   
print(combined_tuple)    

# Create a tuple of your favorite movies, and then write code to print the first two movies and the last two movies in the tuple.

movielist= ('Jigra', 'Fighter', 'Intersteller', 'Dhamal', 'Seal team')
first_two = movielist[:2]
last_two = movielist[-2:]
print("First two movies:", first_two)
print("Last two movies:", last_two)

# Given three tuples, concatenate them into a single tuple while maintaining their original order.

def concatnate(tuple1, tuple2, tuple3):
    return tuple1 + tuple2 + tuple3
    
tuple1= ('hello', 'kofeekodes', 'surat') 
tuple2= (25,123,4)
tuple3= ('vishal','rakshit', 'viraj')   
result= concatnate(tuple1, tuple2, tuple3)
print(result)

# Write a program that asks the user to enter their name, age, and city, and then packs these values into a tuple and prints it.

def get_user_info():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    city = input("Please enter your city: ")
    return (name, age, city)

user_info = get_user_info()
print("User Info:", user_info)

get_user_info()


#Create two tuples, one containing names and the other containing ages. Use the zip function to create a list of tuples where each tuple contains a name and an age.

def tuplelist(name,age):
    return list(zip(name,age))

name = ('vishal', 'rakshit', 'viraj')
age = (22, 23,26)  
name_age= tuplelist(name,age)
print(name_age)
