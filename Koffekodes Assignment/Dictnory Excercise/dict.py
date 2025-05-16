
# Write a function that takes a dictionary of student names and their corresponding scores as input and returns the name of the student with the highest score.

def get_highest_scorer(student_scores):
    if not student_scores:
        return None
    highest_scorer = max(student_scores, key=student_scores.get)
    return f"{highest_scorer} score {student_scores[highest_scorer]}"

student_scores = {}
while True:
    print("Type No if not to add")
    name = input("enter student's name: ")
    if name.lower() == 'No':
        break
    score = int(input("enter student's score: "))
    student_scores[name] = score

print(get_highest_scorer(student_scores))


# Given two dictionaries, merge them into a new dictionary, and in case of overlapping keys, combine their values into a list.

def merge_dicts(dict1, dict2):
    merge_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merge_dict:
            if isinstance(merge_dict[key], list):
                merge_dict[key].append(value)
            else:
                merge_dict[key] = [merge_dict[key], value]
        else:
            merge_dict[key] = value
    return merge_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
merge_dict = merge_dicts(dict1, dict2)
print(merge_dict)


# Create a dictionary of products and their prices. Write a program that asks the user for a product name and checks if it exists in the dictionary. If it does, print its price; otherwise, display an error message.

def dicts():
    products = {
        "apple": 1.00,
        "banana": 0.50,
        "mango": 1.50,
        "kiwi": 2.00
    }

    while True:
        product_name = input("enter product name (or 'No' to exit): ")
        if product_name.lower() == 'No':
            break
        if product_name in products:
            print(f"price of {product_name} is ${products[product_name]:.2f}")
        else:
            print(f"Error: {product_name} not in the product list.")
            
            break
dicts()


# Write a function that takes two dictionaries as input and returns a new dictionary containing key-value pairs that exist in both input dictionaries.
def dicts(dict1, dict2):
    return {key: value for key, value in dict1.items() if key in dict2 and dict2[key] == value}

dict1 = {"Name": "Vishal", "Age": 22}
dict2 = {"Name": "rakshit", "Age": 22}

#kwargs
newdict = {**dict1, **dict2}

print(newdict)
print(dicts(dict1, dict2))


#Given a list of names, create a dictionary where the keys are the names, and the values are the lengths of the names, using a dictionary comprehension.
# Length of the Key
names = ["Vishal", "Rakshit", "Viraj", "Kofeekodes"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)