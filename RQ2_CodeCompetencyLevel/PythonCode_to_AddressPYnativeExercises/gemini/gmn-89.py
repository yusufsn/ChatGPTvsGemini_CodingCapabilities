list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

# Find the innermost list to append the sublist to
for sublist in list1:
    if isinstance(sublist, list):
        for inner_sublist in sublist:
            if isinstance(inner_sublist, list):
                inner_sublist.extend(sub_list)

print(list1)
