def merge_lists(list1, list2):
    # Extract odd numbers from the first list
    odd_numbers = [num for num in list1 if num % 2 != 0]
    # Extract even numbers from the second list
    even_numbers = [num for num in list2 if num % 2 == 0]
    # Combine the two lists
    return odd_numbers + even_numbers

# Given lists
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# Merge lists based on the condition
result_list = merge_lists(list1, list2)

# Display the result
print("Result list:", result_list)
