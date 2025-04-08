from datetime import datetime

# Given date
given_date = datetime(2020, 7, 26)

# Get the day of the week
day_of_week = given_date.strftime("%A")

# Print the day of the week
print(day_of_week)
