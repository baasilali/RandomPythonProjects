#Baasil Ali
#12 / 14 / 2022
#
# This program uses functions to calculate the distance from San Jose to Chicago
# and the distance from Chicago to Washington D.C. and prints the distance in both
# miles and kilometers, properly labeled as integers.

import math

# Function to calculate the great circle distance between two cities
def great_circle_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Calculate the central angle in radians
    theta = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1 - lon2)))

    # Set the radius of the earth in kilometers
    R = 6371

    # Calculate the distance in kilometers
    distance = R * theta

    # Return the distance in kilometers
    return distance

# Function to convert kilometers to miles
def km_to_miles(distance):
    # One kilometer is 0.621371 miles
    return distance * 0.621371

# Calculate the distance from San Jose to Chicago
san_jose = (37.33, -121.9)
chicago = (41.83, -87.68)
distance_km = great_circle_distance(san_jose[0], san_jose[1], chicago[0], chicago[1])
distance_miles = km_to_miles(distance_km)

# Print the distances in both miles and kilometers
print("The distance from San Jose to Chicago is", int(distance_miles), "miles or", int(distance_km), "kilometers.")

# Calculate the distance from Chicago to Washington, D.C.
chicago = (41.83, -87.68)
washington_dc = (38.9, -77.02)
distance_km = great_circle_distance(chicago[0], chicago[1], washington_dc[0], washington_dc[1])
distance_miles = km_to_miles(distance_km)

# Print the distances in both miles and kilometers
print("The distance from Chicago to Washington, D.C. is ", int(distance_miles), "miles or", int(distance_km), "kilometers.")
