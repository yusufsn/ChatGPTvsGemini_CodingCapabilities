list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# Use nested loops to combine elements from both lists
result = []
for word1 in list1:
    for word2 in list2:
        result.append(word1 + word2)

print(result)
