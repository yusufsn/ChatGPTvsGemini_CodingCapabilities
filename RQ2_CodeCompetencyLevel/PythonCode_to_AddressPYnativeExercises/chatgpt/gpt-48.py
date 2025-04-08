# Outer function
def outer_function(a, b):
    # Inner function to calculate addition
    def inner_function(x, y):
        return x + y
    
    # Calculate addition using inner function
    addition = inner_function(a, b)
    
    # Add 5 to the addition and return the result
    return addition + 5

# Function call
result = outer_function(10, 20)
print(result)
