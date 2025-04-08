# Given lists
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

# Picking odd-index elements from l1 and even-index elements from l2
odd_index_l1 = l1[1::2]  # Odd-index items from list l1
even_index_l2 = l2[::2]  # Even-index items from list l2

# Combine both lists to form the final third list
l3 = odd_index_l1 + even_index_l2

# Output the result
print("Element at odd-index positions from list one:")
print(odd_index_l1)
print("Element at even-index positions from list two:")
print(even_index_l2)
print("Printing Final third list:")
print(l3)
