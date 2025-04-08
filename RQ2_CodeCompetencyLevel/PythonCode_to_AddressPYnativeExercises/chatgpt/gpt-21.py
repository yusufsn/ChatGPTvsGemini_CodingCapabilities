# Open the original file for reading
with open('test.txt', 'r') as file:
    lines = file.readlines()

# Open the new file for writing
with open('new_file.txt', 'w') as new_file:
    for i, line in enumerate(lines):
        # Skip line number 5 (index 4)
        if i != 4:
            new_file.write(line)
