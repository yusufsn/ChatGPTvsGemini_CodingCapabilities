tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

# Sort the tuple of tuples by the second element
sorted_tuple = sorted(tuple1, key=lambda x: x[1])

print(sorted_tuple)
