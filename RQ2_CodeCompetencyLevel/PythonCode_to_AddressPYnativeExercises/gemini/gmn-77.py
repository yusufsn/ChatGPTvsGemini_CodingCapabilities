def remove_intersection(first_set, second_set):
  """Removes the intersection of two sets from the first set.

  Args:
    first_set: The first set.
    second_set: The second set.

  Returns:
    The first set after removing the intersection.
  """

  intersection = first_set.intersection(second_set)
  first_set -= intersection
  return first_set

# Example usage
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

intersection = first_set.intersection(second_set)
print("Intersection is", intersection)  

first_set = remove_intersection(first_set, second_set)
print("First Set after removing common element", first_set)
