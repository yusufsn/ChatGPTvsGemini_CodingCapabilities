import datetime

given_date = datetime.datetime(2020, 2, 25)

# Subtract 7 days from the given date
one_week_ago = given_date - datetime.timedelta(days=7)

print(one_week_ago)  # Output: 2020-02-18
