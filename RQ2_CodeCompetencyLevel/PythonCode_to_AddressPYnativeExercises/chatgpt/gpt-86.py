# Given lists
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# Iterate both lists simultaneously
for item1, item2 in zip(list1, list2[::-1]):
    print(item1, item2)
