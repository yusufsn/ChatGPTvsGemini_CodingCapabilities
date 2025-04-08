def func1(*args):
    """Prints the values of all arguments passed to the function.

    Args:
        *args: A variable number of arguments.
    """

    print("Printing values")
    for arg in args:
        print(arg)

# Call the function with different number of arguments
func1(20, 40, 60)
func1(80, 100)
