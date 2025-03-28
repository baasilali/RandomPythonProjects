#Baasil Ali
# 12 / 15 / 2022
#
# Final project. Find the population of a city based on a text file.

def capitalize_city(city):
    """
    Capitalize each word in the given city name, leaving the rest in lower case.
    
    :param city: The city name to capitalize.
    :return: The capitalized city name.
    """
    # Split the city name on the spaces to get each word
    words = city.split(' ')
    # Capitalize each word and join them back together
    return ' '.join([word.capitalize() for word in words])

# lastname_firstname_cities.py

# Open the cities.txt file
with open('cities.txt', 'r') as f:
    # Create a dictionary where the key is the city name and the value is a list
    # containing the country and population
    cities = {}
    for line in f:
        # Split the line on the commas to get the city, country, and population
        city, country, population = line.strip().split(',')
        # Add the city to the dictionary with the capitalized name as the key and
        # the country and population as the value
        cities[capitalize_city(city)] = [country, int(population)]

# Print the total number of cities
print('Number of cities: %.2f ' % len(cities))

# Calculate the sum of all the city populations
total_population = 0
for city, info in cities.items():
    total_population += info[1]

# Calculate the average population
average_population = total_population / len(cities)

# Print the average population
print('Average population:',  average_population)

# Ask the user to repeatedly enter city names, or just press ENTER to quit
while True:
    city = input('Enter a city, or just ENTER to quit: ')

    # If the user just pressed ENTER, quit the program
    if not city:
        break

    # If the city is in the dictionary, print its information
    if city in cities:
        country, population = cities[city]
        print(city, ' is in ', country, ' and has a population of ', population)
    else:
        # Otherwise, print a message saying that the city was not found
        print(city, ' was not found in the database.')
