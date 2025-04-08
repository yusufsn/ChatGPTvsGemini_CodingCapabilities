from datetime import datetime
from dateutil.relativedelta import relativedelta

# Given date
given_date = datetime(2020, 2, 25).date()

# Add 4 months to the given date
new_date = given_date + relativedelta(months=+4)

# Print the new date
print(new_date)
