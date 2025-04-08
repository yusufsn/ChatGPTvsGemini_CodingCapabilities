import datetime

date_string = "Feb 25 2020 4:20PM"

# Parse the date string using strptime
datetime_object = datetime.datetime.strptime(date_string, "%b %d %Y %I:%M%p")

print(datetime_object)  # Output: 2020-02-25 16:20:00
