list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# Find the index of 6000 within the nested list
for sublist in list1:
    if isinstance(sublist, list):
        for inner_sublist in sublist:
            if isinstance(inner_sublist, list):
                if 6000 in inner_sublist:
                    index = inner_sublist.index(6000) + 1
                    inner_sublist.insert(index, 7000)

print(list1)
