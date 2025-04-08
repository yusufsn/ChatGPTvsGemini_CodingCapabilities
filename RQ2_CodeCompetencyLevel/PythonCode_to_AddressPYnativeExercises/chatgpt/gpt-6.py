def display_divisible_by_five(numbers):
    print("Given list is", numbers)
    print("Divisible by 5")
    for num in numbers:
        if num % 5 == 0:
            print(num)

# Example usage
numbers = [10, 20, 33, 46, 55]
display_divisible_by_five(numbers)
