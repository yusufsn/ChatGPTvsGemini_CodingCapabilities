# Given sets
first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

# Check if first set is a subset of second set
is_subset_first = first_set.issubset(second_set)
print("First set is subset of second set -", is_subset_first)

# Check if second set is a subset of first set
is_subset_second = second_set.issubset(first_set)
print("Second set is subset of First set -", is_subset_second)

# Check if first set is a superset of second set
is_superset_first = first_set.issuperset(second_set)
print("First set is Super set of second set -", is_superset_first)

# Check if second set is a superset of first set
is_superset_second = second_set.issuperset(first_set)
print("Second set is Super set of First set -", is_superset_second)

# If first set is subset or superset, delete all elements
if is_subset_first or is_superset_first:
    first_set.clear()

# If second set is subset or superset, delete all elements
if is_subset_second or is_superset_second:
    second_set.clear()

# Output the final sets
print("First Set", first_set)
print("Second Set", second_set)
