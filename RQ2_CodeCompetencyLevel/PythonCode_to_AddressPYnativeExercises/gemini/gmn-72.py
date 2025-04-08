def merge_odd_even_indices(l1, l2):
  """Merges odd-indexed elements from l1 and even-indexed elements from l2.

  Args:
    l1: The first list.
    l2: The second list.

  Returns:
    A new list containing the merged elements.
  """

  l3 = []
  for i in range(1, len(l1), 2):
    l3.append(l1[i])
  for i in range(0, len(l2), 2):
    l3.append(l2[i])
  return l3

# Example usage
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = merge_odd_even_indices(l1, l2)

print("Element at odd-index positions from list one")
print(l1[1::2])
print("Element at even-index positions from list two")
print(l2[::2])
print("\nPrinting Final third list")
print(l3)
