# Open the file for reading
with open('test.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

# Access and print line number 4 (index 3)
print("Line number 4:", lines[3].strip())  # strip() removes any leading/trailing whitespace
