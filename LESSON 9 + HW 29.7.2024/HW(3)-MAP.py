# HOMEWORK 3 MAP

# MAP:
# 3. Create a list of 20 random numbers between -50 and +50:
# Use map and lambda for various transformations:
# 1. Each number raised to the power of 3
# 2. Only the ones digit of each number (e.g., 42 becomes 2)
# 3. Each number converted to Fahrenheit (i.e., multiply by 9/5 and add 32)
# 4. Each positive number becomes “positive”
# and each negative number becomes “negative”
# 5. The largest number is replaced with
# “max” and the smallest with “min”, the rest remain unchanged
# 6. Bonus: Each number with its digits reversed
# 7. Bonus: Each number as its absolute value
# (positive stays positive, negative becomes positive)
# 8. Bonus: Create a list of monthly incomes and expenses.
# The first number is income and the second is expenses.

# START

# 3. Create a list of 20 random numbers between -50 and +50:
import random

numbers = [random.randint(-50, 50) for _ in range(20)]
print("Original list:", numbers)

# 1. Each number raised to the power of 3
cubed_numbers = list(map(lambda x: x ** 3, numbers))
print("Cubed numbers:", cubed_numbers)

# 2. Only the ones digit of each number (e.g., 42 becomes 2)
ones_digit_numbers = list(map(lambda x: abs(x) % 10, numbers))
print("Ones digit of each number:", ones_digit_numbers)

# 3. Each number converted to Fahrenheit (i.e., multiply by 9/5 and add 32)
fahrenheit_numbers = list(map(lambda x: x * 9/5 + 32, numbers))
print("Numbers in Fahrenheit:", fahrenheit_numbers)

# 4. Each positive number becomes “positive”
# and each negative number becomes “negative”
positivity = list(map(lambda x: "positive" if x > 0 else "negative", numbers))
print("Positive/Negative mapping:", positivity)

# 5. The largest number is replaced with
# “max” and the smallest with “min”, the rest remain unchanged
max_number = max(numbers)
min_number = min(numbers)
max_min_mapping = list(map(lambda x: "max" if x == max_number else ("min" if x == min_number else x), numbers))
print("Max/Min mapping:", max_min_mapping)

# 6. Bonus: Each number with its digits reversed
reversed_numbers = list(map(lambda x: int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1]), numbers))
print("Reversed digit numbers:", reversed_numbers)

# 7. Bonus: Each number as its absolute value
# (positive stays positive, negative becomes positive)
absolute_numbers = list(map(lambda x: abs(x), numbers))
print("Absolute value of numbers:", absolute_numbers)

# 8. Bonus: Create a list of monthly incomes and expenses.
# The first number is income and the second is expenses.
income_expense = [
    [10000, 7000],
    [3000, 5000],
    [2000, 8000]
]
monthly_balance = list(map(lambda x: x[0] - x[1], income_expense))
print("Monthly balance:", monthly_balance)

# END