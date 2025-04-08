def calculate_income_tax(income):
    tax = 0
    
    # First $10,000 is taxed at 0%
    if income > 10000:
        tax += 10000 * 0
        income -= 10000
    else:
        tax += income * 0
        return tax
    
    # Next $10,000 is taxed at 10%
    if income > 10000:
        tax += 10000 * 0.10
        income -= 10000
    else:
        tax += income * 0.10
        return tax
    
    # The remaining income is taxed at 20%
    tax += income * 0.20
    return tax

# Example usage
income = 45000
tax_payable = calculate_income_tax(income)

# Display the result
print(f"For an income of ${45000}, the income tax payable is ${tax_payable}")
