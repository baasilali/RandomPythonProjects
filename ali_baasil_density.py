# Baasil Ali
# 12 / 14 / 2022
#
# This program will read in numbers 
# from a text file into a list and then properly
# prints the minimun, maximum, average, and median
# densities.
# Open the file and read the numbers into a list

with open('density.txt') as f:
    data = [line.strip() for line in f]

# Separate the planet name from the density by splitting each line on the colon
data = [line.split(' ')[1] for line in data]

# Convert the densities from strings to floats
data = [float(x) for x in data]

# Calculate the minimum, maximum, and average densities
min_density = min(data)
max_density = max(data)
avg_density = sum(data) / len(data)

# Print the results
print('Minimum density: %.2f' % min_density)
print('Maximum density: %.2f' % max_density)
print('Average density: %.2f' % avg_density)

# Sort the densities in ascending order
data.sort()

# Calculate the median density
if len(data) % 2 == 1:
    # If the list has an odd number of elements, the median is the middle element
    median_density = data[(len(data) - 1) // 2]
else:
    # If the list has an even number of elements, the median is the average of the two middle elements
    median_density = (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2

# Print the median density
print('Median density: %.2f' % median_density)


