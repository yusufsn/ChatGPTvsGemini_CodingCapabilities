# Accept input from the user
user_string = input("Enter a string: ")

print("Original String is", user_string)
print("Printing only even index chars")

# Loop through the string to extract characters at even indices
for index in range(0, len(user_string), 2):
    print(user_string[index])
