tuple1 = (45, 45, 45, 45)

# Check if all items in the tuple are the same
all_same = all(item == tuple1[0] for item in tuple1)

# Display the result
print(all_same)  # should print True
