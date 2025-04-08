from datetime import datetime

# Given dates
date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)

# Calculate the difference between the two dates
date_difference = date_2 - date_1

# Print the number of days
print(date_difference.days)  # Expected output: 205
