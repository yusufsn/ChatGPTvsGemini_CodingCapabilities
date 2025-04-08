from datetime import datetime, timedelta

# Given date
given_date = datetime(2020, 2, 25)

# Subtract 7 days (1 week)
new_date = given_date - timedelta(days=7)

# Print the new date
print(new_date.strftime("%Y-%m-%d"))
