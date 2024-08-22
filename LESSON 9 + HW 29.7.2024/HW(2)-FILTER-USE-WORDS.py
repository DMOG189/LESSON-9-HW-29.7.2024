# HOMEWORK 2 FILTER

# FILTER:
# 2. Create the list of games:
# 1. Only games with names longer than 8 characters
# 2. Only games whose names start with the letter F
# 3. Only games whose names contain exactly 2 words
# 4. Only games whose names contain the letter V
# 5. Bonus: Only games that contain special characters such as “:!^&*”
# 6. Bonus: Add the release year for each game.
# Then keep only the games released after 2014

# START

# 2. Create the list of games:
games = [
    "Grand Theft Auto V",
    "Fortnite",
    "The Elder Scrolls V: Skyrim",
    "Dark Souls",
    "Overwatch"
]

# 1. Only games with names longer than 8 characters
long_name_games = list(filter(lambda x: len(x) > 8, games))
print("Games with names longer than 8 characters:", long_name_games)

# 2. Only games whose names start with the letter F
games_starting_with_F = list(filter(lambda x: x.startswith('F'), games))
print("Games starting with the letter F:", games_starting_with_F)

# 3. Only games whose names contain exactly 2 words
two_word_games = list(filter(lambda x: len(x.split()) == 2, games))
print("Games with exactly 2 words in their name:", two_word_games)

# 4. Only games whose names contain the letter V
games_with_V = list(filter(lambda x: 'V' in x, games))
print("Games containing the letter V:", games_with_V)

# 5. Bonus: Only games that contain special characters such as “:!^&*”
special_characters = ":!^&*"
games_with_special_chars = list(filter(lambda x: any(char in x for char in special_characters), games))
print("Games containing special characters:", games_with_special_chars)

# 6. Bonus: Add the release year for each game.
# Then keep only the games released after 2014
games_with_years = [
    ["Grand Theft Auto V", 2013],
    ["Fortnite", 2017],
    ["The Elder Scrolls V: Skyrim", 2011],
    ["Dark Souls", 2011],
    ["Overwatch", 2016]
]

games_after_2014 = list(filter(lambda x: x[1] > 2014, games_with_years))
print("Games released after 2014:", games_after_2014)

# END