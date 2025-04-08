list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# Create a new list to store the concatenated strings
result = []

# Iterate through both lists simultaneously
for i in range(min(len(list1), len(list2))):
    result.append(list1[i] + list2[i])

# Add any remaining elements from the longer list
result.extend(list1[len(list2):])
result.extend(list2[len(list1):])

print(result)
