# Given list
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# Add 7000 after 6000
list1[2][2].insert(list1[2][2].index(6000) + 1, 7000)

# Display the result
print(list1)
