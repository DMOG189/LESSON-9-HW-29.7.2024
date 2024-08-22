# HOMEWORK 4 MAP

# MAP:
# 4. Create the list of fruits:
# Use map and lambda for various transformations:
# 1. Each fruit with its letters in reverse order
# 2. The first letter of each fruit
# 3. Each fruit name in uppercase
# 4. The length of each fruit’s name (e.g., Apple becomes 5)
# 5. Bonus: If the fruit ends with
# ‘s’, add an exclamation mark; otherwise, keep it the same
# 6. Bonus: Add the number of calories per 100 grams for each fruit:
## a. Create a new list that contains only the number of calories
## b. Create a new list with
## fruit names combined with calories, e.g., "52Apple"
## c. Same list but if a fruit has more than 50 calories,
## add an exclamation mark to its name



# START

# 4. Create the list of fruits:
fruits = ["Mango", "Orange", "Banana", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"]

# 1. Each fruit with its letters in reverse order
reversed_fruits = list(map(lambda x: x[::-1], fruits))
print("Fruits with letters reversed:", reversed_fruits)

# 2. The first letter of each fruit
first_letter_fruits = list(map(lambda x: x[0], fruits))
print("First letter of each fruit:", first_letter_fruits)

# 3. Each fruit name in uppercase
uppercase_fruits = list(map(lambda x: x.upper(), fruits))
print("Fruits in uppercase:", uppercase_fruits)

# 4. The length of each fruit’s name (e.g., Apple becomes 5)
length_of_fruits = list(map(lambda x: len(x), fruits))
print("Length of each fruit's name:", length_of_fruits)

# 5. Bonus: If the fruit ends with
# ‘s’, add an exclamation mark; otherwise, keep it the same
fruits_with_exclamation = list(map(lambda x: x + "!" if x.endswith('s') else x, fruits))
print("Fruits with exclamation if ending with 's':", fruits_with_exclamation)

# 6. Bonus: Add the number of calories per 100 grams for each fruit:
fruits_with_calories = [
    ["Apple", 52],
    ["Banana", 89],
    ["Orange", 47],
    ["Mango", 60],
    ["Strawberry", 32],
    ["Pineapple", 50],
    ["Grapes", 69],
    ["Watermelon", 30]
]

# a. Create a new list that contains only the number of calories
calories_only = list(map(lambda x: x[1], fruits_with_calories))
print("Calories for each fruit:", calories_only)

# b. Create a new list with fruit names combined with calories, e.g., "52Apple"
combined_fruits_calories = list(map(lambda x: str(x[1]) + x[0], fruits_with_calories))
print("Fruits combined with calories:", combined_fruits_calories)

# c. Same list but if a fruit has more than 50 calories, add an exclamation mark to its name
fruits_with_calories_exclamation = list(map(lambda x: str(x[1]) + x[0] + "!" if x[1] > 50 else str(x[1]) + x[0], fruits_with_calories))
print("Fruits combined with calories and exclamation if >50:", fruits_with_calories_exclamation)


# END