# Given number of terms
n = 5

# Initialize the sum of the series
total_sum = 0

# Loop to calculate the sum of the series
for i in range(1, n + 1):
    term = int("2" * i)  # Create the term by repeating '2' i times
    total_sum += term  # Add the term to the total sum

# Print the result
print(total_sum)
