def check_and_delete(first_set, second_set):
  """Checks subset/superset relationships and deletes elements accordingly.

  Args:
    first_set: The first set.
    second_set: The second set.

  Returns:
    None. Modifies the sets in-place.
  """

  if first_set.issubset(second_set):
    print("First set is subset of second set - True")
    first_set.clear()
  else:
    print("First set is subset of second set - False")

  if second_set.issubset(first_set):
    print("Second set is subset of First set - True")
    second_set.clear()
  else:
    print("Second set is subset of First set - False")

  if first_set.issuperset(second_set):
    print("First set is Super set of second set - True")
    second_set.clear()
  else:
    print("First set is Super set of second set - False")

  if second_set.issuperset(first_set):
    print("Second set is Super set of First set - True")
    first_set.clear()
  else:
    print("Second set is Super set of First set - False")

# Example usage
first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

check_and_delete(first_set, second_set)

print("First Set", first_set)
print("Second Set", second_set)
