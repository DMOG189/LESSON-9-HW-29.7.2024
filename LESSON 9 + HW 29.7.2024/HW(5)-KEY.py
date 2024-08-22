# HOMEWORK 5 KEY

# KEY:
# 5. Create the list of cities:
# Use sort and lambda for various sorting tasks
# 1. Sort by the length of the city name
# 2. Sort by the last letter of the city name
# 3. Sort by the city name in reverse order (i.e., reverse the letters of the name)
# 4. Bonus: Add the distance from Israel in miles and the continent name
# a. Sort by the distance from Israel
# b. Sort by the distance from Israel from largest to smallest
# c. Sort by the continent name
# d. Sort by continent name, and within each continent, sort by distance

# START

# 5. Create the list of cities:
cities = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]

# 1. Sort by the length of the city name
cities.sort(key=lambda x: len(x))
print("Cities sorted by length of name:", cities)

# 2. Sort by the last letter of the city name
cities.sort(key=lambda x: x[-1])
print("Cities sorted by the last letter of name:", cities)

# 3. Sort by the city name in reverse order (i.e., reverse the letters of the name)
cities.sort(key=lambda x: x[::-1])
print("Cities sorted by reverse name order:", cities)

# 4. Bonus: Add the distance from Israel in miles and the continent name
cities_with_details = [
    ["Tokyo", 5760, "Asia"],
    ["New York", 5690, "North America"],
    ["Paris", 2050, "Europe"],
    ["London", 2240, "Europe"],
    ["Sydney", 8780, "Australia"],
    ["Dubai", 1300, "Asia"],
    ["Shanghai", 4920, "Asia"]
]

# a. Sort by the distance from Israel
cities_with_details.sort(key=lambda x: x[1])
print("Cities sorted by distance from Israel:", cities_with_details)

# b. Sort by the distance from Israel from largest to smallest
cities_with_details.sort(key=lambda x: x[1], reverse=True)
print("Cities sorted by distance from Israel (largest to smallest):", cities_with_details)

# c. Sort by the continent name
cities_with_details.sort(key=lambda x: x[2])
print("Cities sorted by continent name:", cities_with_details)

# d. Sort by continent name, and within each continent, sort by distance
cities_with_details.sort(key=lambda x: (x[2], x[1]))
print("Cities sorted by continent and then by distance:", cities_with_details)

# END