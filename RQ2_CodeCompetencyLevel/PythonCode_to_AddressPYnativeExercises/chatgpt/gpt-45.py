# Function with variable length of arguments
def func1(*args):
    print("Printing values")
    for arg in args:
        print(arg)

# Function calls with different numbers of arguments
func1(20, 40, 60)  # 3 arguments
func1(80, 100)     # 2 arguments
