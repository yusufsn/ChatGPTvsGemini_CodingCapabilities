def is_palindrome_number(number):
    # Convert the number to a string
    str_number = str(number)
    # Check if the string is the same when reversed
    if str_number == str_number[::-1]:
        return True
    else:
        return False

# Example usage
number1 = 121
print(f"Original number {number1}")
if is_palindrome_number(number1):
    print("Yes, the given number is a palindrome number")
else:
    print("No, the given number is not a palindrome number")

number2 = 125
print(f"Original number {number2}")
if is_palindrome_number(number2):
    print("Yes, the given number is a palindrome number")
else:
    print("No, the given number is not a palindrome number")
