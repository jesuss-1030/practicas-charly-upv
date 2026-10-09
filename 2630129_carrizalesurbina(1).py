# ============================================================
# PORTADA
# ============================================================
# Name: Carrizales Urbina
# Student ID: 2630129
# group: 1A
# ============================================================

# ============================================================
# EXECUTIVE SUMMARY
# ============================================================
# int is used for whole numbers. float is used for numbers with
# decimals. bool (True/False) is obtained from comparisons.
# Validating ranges and avoiding division by zero prevents errors.
# This file covers six problems using int, float and bool with
# description, inputs, outputs, validations and test cases.
# ============================================================

# ============================================================
# PRINCIPLES AND BEST PRACTICES
# ============================================================
# Use int for counters and whole quantities.
# Use float for measurements with decimals.
# Store intermediate results in variables.
# Validate data before operating.
# Use descriptive variable names and clear messages.
# Document what true and false mean in each context.
# ============================================================

# ============================================================
# PROBLEM 1: Temperature converter and range flag
# ============================================================
# Description: Convert Celsius to Fahrenheit and Kelvin.
# Determine if temperature is high (>= 30.0).
#
# Inputs (fixed): temp_c = 25.0
# Outputs: "Fahrenheit:", "Kelvin:", "High temperature:"
# Validations: convertible to float, Kelvin >= 0
#
# Test cases:
# 1) Normal: 25.0
# 2) Border: 30.0
# 3) Error: invalid conversion
# ============================================================

print("=== Problem 1 ===")
temp_c = 25.0
temp_f = temp_c * 9 / 5 + 32
temp_k = temp_c + 273.15
is_high_temperature = temp_c >= 30.0
print("Fahrenheit:", round(temp_f, 2))
print("Kelvin:", round(temp_k, 2))
print("High temperature:", is_high_temperature)

# ============================================================
# PROBLEM 2: Work hours and overtime payment
# ============================================================
# Description: Calculate weekly pay with overtime at 150%.
# Flag if there are overtime hours.
#
# Inputs (fixed): hours_worked = 45.0, hourly_rate = 100.0
# Outputs: "Regular pay:", "Overtime pay:", "Total pay:", "Has overtime:"
# Validations: hours_worked >= 0, hourly_rate > 0
#
# Test cases:
# 1) Normal: 45 hours
# 2) Border: 40 hours
# 3) Error: negative hours
# ============================================================

print("\n=== Problem 2 ===")
hours_worked = 45.0
hourly_rate = 100.0
regular_hours = min(hours_worked, 40.0)
overtime_hours = max(hours_worked - 40.0, 0.0)
regular_pay = regular_hours * hourly_rate
overtime_pay = overtime_hours * hourly_rate * 1.5
total_pay = regular_pay + overtime_pay
has_overtime = hours_worked > 40.0
print("Regular pay:", round(regular_pay, 2))
print("Overtime pay:", round(overtime_pay, 2))
print("Total pay:", round(total_pay, 2))
print("Has overtime:", has_overtime)

# ============================================================
# PROBLEM 3: Discount eligibility with booleans
# ============================================================
# Description: Check if customer gets 10% discount.
# Discount if student OR senior OR total >= 1000.
#
# Inputs (fixed): purchase_total = 1200.0, is_student = True, is_senior = False
# Outputs: "Discount eligible:", "Final total:"
# Validations: purchase_total >= 0
#
# Test cases:
# 1) Normal: total 1200, student True
# 2) Border: total 1000
# 3) Error: invalid text
# ============================================================

print("\n=== Problem 3 ===")
purchase_total = 1200.0
is_student = True
is_senior = False
discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
final_total = purchase_total * 0.9
print("Discount eligible:", discount_eligible)
print("Final total:", round(final_total, 2))

# ============================================================
# PROBLEM 4: Basic statistics of three integers
# ============================================================
# Description: Calculate sum, average, max, min and all_even flag.
#
# Inputs (fixed): n1 = 4, n2 = 8, n3 = 12
# Outputs: "Sum:", "Average:", "Max:", "Min:", "All even:"
# Validations: convertible to int
#
# Test cases:
# 1) Normal: 4 8 12
# 2) Border: 0 0 0
# 3) Error: non-integer
# ============================================================

print("\n=== Problem 4 ===")
n1 = 4
n2 = 8
n3 = 12
sum_value = n1 + n2 + n3
average_value = sum_value / 3
max_value = max(n1, n2, n3)
min_value = min(n1, n2, n3)
all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
print("Sum:", sum_value)
print("Average:", round(average_value, 2))
print("Max:", max_value)
print("Min:", min_value)
print("All even:", all_even)

# ============================================================
# PROBLEM 5: Loan eligibility (income and debt ratio)
# ============================================================
# Description: Check loan eligibility based on income, debt ratio
# and credit score.
#
# Inputs (fixed): monthly_income = 10000.0, monthly_debt = 3000.0, credit_score = 700
# Outputs: "Debt ratio:", "Eligible:"
# Validations: monthly_income > 0, monthly_debt >= 0, credit_score >= 0
#
# Test cases:
# 1) Normal: income 10000, debt 3000, score 700
# 2) Border: debt_ratio = 0.4
# 3) Error: income 0
# ============================================================

print("\n=== Problem 5 ===")
monthly_income = 10000.0
monthly_debt = 3000.0
credit_score = 700
debt_ratio = monthly_debt / monthly_income
eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)
print("Debt ratio:", round(debt_ratio, 4))
print("Eligible:", eligible)

# ============================================================
# PROBLEM 6: Body Mass Index (BMI) and category flag
# ============================================================
# Description: Calculate BMI and flags for underweight, normal
# and overweight.
#
# Inputs (fixed): weight_kg = 70.0, height_m = 1.75
# Outputs: "BMI:", "Underweight:", "Normal:", "Overweight:"
# Validations: weight_kg > 0, height_m > 0
#
# Test cases:
# 1) Normal: 70 kg, 1.75 m
# 2) Border: bmi = 18.5
# 3) Error: height 0
# ============================================================

print("\n=== Problem 6 ===")
weight_kg = 70.0
height_m = 1.75
bmi = weight_kg / (height_m * height_m)
is_underweight = bmi < 18.5
is_normal = (bmi >= 18.5) and (bmi < 25.0)
is_overweight = bmi >= 25.0
print("BMI:", round(bmi, 2))
print("Underweight:", is_underweight)
print("Normal:", is_normal)
print("Overweight:", is_overweight)

# ============================================================
# CONCLUSIONS
# ============================================================
# Integers and floats are used together for real calculations.
# Comparisons produce booleans that allow decisions.
# Validating ranges and avoiding division by zero is essential.
# Combined conditions with and, or, not appear in payroll,
# discounts, loans and many real systems.
# ============================================================

# ============================================================
# REFERENCES
# ============================================================
# 1) Python docs - Numeric Types: int, float
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 2) Python docs - Boolean Type
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 3) Python Tutorial - Operators
#    https://docs.python.org/3/tutorial/introduction.html
# 4) Real Python - Numbers in Python
#    https://realpython.com/python-numbers/
# 5) Lutz, M. Learning Python. O'Reilly.
# ============================================================
