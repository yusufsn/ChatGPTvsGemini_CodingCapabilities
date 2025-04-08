# Function with a default argument for salary
def show_employee(name, salary=9000):
    print(f"Name: {name} salary: {salary}")

# Function calls
show_employee("Ben", 12000)  # Salary provided
show_employee("Jessa")       # Salary not provided, defaults to 9000
