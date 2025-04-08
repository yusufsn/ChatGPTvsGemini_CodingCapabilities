list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# Iterate both lists simultaneously, reversing the order of list2
for item1, item2 in zip(list1, reversed(list2)):
    print(item1, item2)
