# Given list
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Remove empty strings from the list
cleaned_list = [item for item in list1 if item != ""]

# Display the result
print(cleaned_list)
