# Given list
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# Sublist to add
sub_list = ["h", "i", "j"]

# Extend the nested list by adding sublist ["h", "i", "j"]
list1[2][1][2].extend(sub_list)

# Display the result
print(list1)
