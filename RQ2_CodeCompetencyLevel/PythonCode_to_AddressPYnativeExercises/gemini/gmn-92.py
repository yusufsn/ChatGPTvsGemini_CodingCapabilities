keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Create a dictionary using dictionary comprehension
result_dict = {key: value for key, value in zip(keys, values)}

print(result_dict)  # Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
