from datetime import datetime

# Given date
given_date = datetime(2020, 2, 25)

# Convert the datetime into a string
date_string = given_date.strftime("%Y-%m-%d %H:%M:%S")

# Print the string representation of the datetime
print(date_string)
