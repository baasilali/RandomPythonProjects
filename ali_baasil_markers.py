# Exam 1 Practice Program
# Baasil Ali
# 10/06/2022


oneMarker = 0.80
packMarker = 3.50
numInPack = 5
tax = 0.065 #percent of total
shipping = 0.05 #pecent of total (before tax)

numMarkers = float(input("How many markers are you buying? "))

packages = numMarkers // numInPack
seperate = numMarkers % numInPack

print("Number of packages: " + str(packages))
print("Number of seperate markers: " + str(seperate))

subtotal = (packages * packMarker) + (seperate * oneMarker)
totalTax = subtotal * tax
totalShipping = subtotal * shipping

total = subtotal + totalTax + totalShipping

print("Subtotal: $%.2f" % subtotal)
print("Tax: $%.2f" % totalTax)
print("Shipping: $%.2f" % totalShipping)
print("Total: $%.2f" % total)



