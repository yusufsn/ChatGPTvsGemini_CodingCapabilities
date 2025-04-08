def count_substring_occurrences(input_string, substring):
    count = input_string.count(substring)
    return count

# Given string
str_x = "Emma is good developer. Emma is a writer"

# Count occurrences of the substring "Emma"
occurrences = count_substring_occurrences(str_x, "Emma")

# Display result
print(f"Emma appeared {occurrences} times")
