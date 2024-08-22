# HOMEWORK 1 FILTER

# FILTER USE:
# Creating a list of 50 random numbers between 1-100
# now use filter and lambda to get:
# 1. Only numbers greater than 50
# 2. Only numbers divisible by 7 without a remainder
# 3. Only two-digit numbers (10-99)`
# 4. Only two-digit numbers where the ones digit equals the tens digit
# 5. Only numbers where the sum of their digits is 9
# 6. Only numbers greater than the average
# 7. Only numbers greater than half of the maximum number in the list
# 8. Bonus: Only numbers greater than the median
# 9. Bonus: Input 5 numbers from the user and insert them into the list.
# Now keep in the list only numbers that are different from the numbers that the user entered
# 10. Bonus: Only prime numbers

# START

# Creating a list of 50 random numbers between 1-100
import random

numbers = [random.randint(1, 100) for _ in range(50)]
print("Original list:", numbers)

# 1. Only numbers greater than 50
greater_than_50 = list(filter(lambda x: x > 50, numbers))
print("Numbers greater than 50:", greater_than_50)

# 2. Only numbers divisible by 7 without a remainder
divisible_by_7 = list(filter(lambda x: x % 7 == 0, numbers))
print("Numbers divisible by 7:", divisible_by_7)

# 3. Only two-digit numbers (10-99)`
two_digit_numbers = list(filter(lambda x: 10 <= x <= 99, numbers))
print("Two-digit numbers:", two_digit_numbers)

# 4. Only two-digit numbers where the ones digit equals the tens digit
same_digit_numbers = list(filter(lambda x: 10 <= x <= 99 and (x // 10) == (x % 10), numbers))
print("Two-digit numbers with the same digits:", same_digit_numbers)

# 5. Only numbers where the sum of their digits is 9
sum_of_digits_9 = list(filter(lambda x: sum(map(int, str(x))) == 9, numbers))
print("Numbers where the sum of digits is 9:", sum_of_digits_9)

# 6. Only numbers greater than the average
average = sum(numbers) / len(numbers)
greater_than_average = list(filter(lambda x: x > average, numbers))
print("Numbers greater than the average:", greater_than_average)

# 7. Only numbers greater than half of the maximum number in the list
half_max = max(numbers) / 2
greater_than_half_max = list(filter(lambda x: x > half_max, numbers))
print("Numbers greater than half the max value:", greater_than_half_max)

# 8. Bonus: Only numbers greater than the median
sorted_numbers = sorted(numbers)
median = sorted_numbers[len(sorted_numbers) // 2] if len(sorted_numbers) % 2 == 0 else (sorted_numbers[len(sorted_numbers) // 2] + sorted_numbers[len(sorted_numbers) // 2 - 1]) / 2
greater_than_median = list(filter(lambda x: x > median, numbers))
print("Numbers greater than the median:", greater_than_median)

# 9. Bonus: Input 5 numbers from the user and insert them into the list.
# Now keep in the list only numbers that are different from the numbers that the user entered
user_numbers = [int(input(f"Enter number {i+1}: ")) for i in range(5)]
unique_numbers = list(filter(lambda x: x not in user_numbers, numbers))
print("Numbers not in user list:", unique_numbers)

# 10. Bonus: Only prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", prime_numbers)

# END