tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

# Sort the tuple by the second item of each inner tuple
sorted_tuple = tuple(sorted(tuple1, key=lambda x: x[1]))

# Display the sorted tuple
print(sorted_tuple)  # should print (('c', 11), ('a', 23), ('d', 29), ('b', 37))
