#sorting list without using built-in function.

# lst = [1,2,3,6,5,4,2]

# for i in range(len(lst)):
#     for j in range(len(lst)-1):
#         if lst[j] > lst[j+1]:
#             lst[j],lst[j+1] = lst[j+1], lst[j]

# print(lst)

################################################################################

# Find minimum and maximum without built-in functions
number = [30,76,50,94,16,25,100,67]
min = number[0]
max = 0

for num in number:
    if num < min:
        min = num
    elif num > max:
        max = num

print("minimum number:", min)
print("maximum number:", max)   

# finding second largest number
number = [30,76,50,94,16,25,100,67]
first = 0
second = 0

for n in number:
    if n > first:
        second = first
        first = n
    elif n != first:
        if second == 0:
            second = n
        elif n > second:
            second = n

print("second big number:", second)

