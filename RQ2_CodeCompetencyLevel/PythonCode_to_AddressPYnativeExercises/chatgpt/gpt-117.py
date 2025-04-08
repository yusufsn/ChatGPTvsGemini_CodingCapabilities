tuple1 = (11, [22, 33], 44, 55)

# Modify the first item of the list inside the tuple
tuple1[1][0] = 222

# Display the modified tuple
print("tuple1:", tuple1)  # should print (11, [222, 33], 44, 55)
