import os

# Specify the file name
file_name = 'new_file.txt'

# Get the file size using os.stat()
file_size = os.stat(file_name).st_size

# Check if the file is empty or not
if file_size == 0:
    print(f"The file '{file_name}' is empty.")
else:
    print(f"The file '{file_name}' is not empty.")
