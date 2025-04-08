def calculate_income_tax(income):
  """Calculates income tax based on the given income.

  Args:
    income: The annual income.

  Returns:
    The total income tax.
  """

  taxable_income = income
  total_tax = 0

  # First $10,000: 0% tax
  if taxable_income > 10000:
    tax = 0
    total_tax += tax
    taxable_income -= 10000

  # Next $10,000: 10% tax
  if taxable_income > 10000:
    tax = 10000 * 0.1
    total_tax += tax
    taxable_income -= 10000

  # Remaining: 20% tax
  if taxable_income > 0:
    tax = taxable_income * 0.2
    total_tax += tax

  return total_tax

# Example usage:
income = 45000
tax = calculate_income_tax(income)
print("Income Tax:", tax)
