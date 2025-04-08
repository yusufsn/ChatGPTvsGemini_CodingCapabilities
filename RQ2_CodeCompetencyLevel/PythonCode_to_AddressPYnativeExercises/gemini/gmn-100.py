sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

# Find the key with the minimum value
min_value_key = min(sample_dict, key=sample_dict.get)

print(min_value_key)  # Output: Math
