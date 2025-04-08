# Given sets
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

# Find the intersection of the two sets
intersection = first_set & second_set

# Output the intersection
print("Intersection is", intersection)

# Remove the common elements from the first set
first_set -= intersection

# Output the first set after removing common elements
print("First Set after removing common element", first_set)
