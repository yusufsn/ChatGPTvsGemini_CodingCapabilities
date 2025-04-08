# Given lists
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

# Create a set of pairs by zipping both lists
result_set = set(zip(first_list, second_list))

# Output the result
print("Result is", result_set)
