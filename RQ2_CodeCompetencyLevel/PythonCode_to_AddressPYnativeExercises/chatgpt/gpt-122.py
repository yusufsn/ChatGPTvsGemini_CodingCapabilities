from datetime import datetime

# Given date string
date_string = "Feb 25 2020 4:20PM"

# Convert the string into a datetime object using strptime
date_object = datetime.strptime(date_string, "%b %d %Y %I:%M%p")

# Print the datetime object in the desired format
print(date_object.strftime("%Y-%m-%d %H:%M:%S"))
