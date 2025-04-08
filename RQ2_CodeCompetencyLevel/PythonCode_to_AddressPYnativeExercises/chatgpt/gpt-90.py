# Given list
list1 = [5, 10, 15, 20, 25, 50, 20]

# Find the first occurrence of 20 and replace it with 200
if 20 in list1:
    list1[list1.index(20)] = 200

# Display the result
print(list1)
