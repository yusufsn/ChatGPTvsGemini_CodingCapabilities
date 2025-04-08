from datetime import datetime, timedelta

# Given date
given_date = datetime(2020, 3, 22, 10, 0, 0)

# Add 7 days and 12 hours
new_date = given_date + timedelta(days=7, hours=12)

# Print the new date and time
print(new_date.strftime("%Y-%m-%d %H:%M:%S"))
