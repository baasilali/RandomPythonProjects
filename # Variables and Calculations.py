# Variables and Calculations
# Baasil Ali
# 09 / 16 / 2022

priceOne = float(input("Enter price for item 1: "))
priceTwo = float(input("Enter price for item 2: "))
priceThree= float(input("Enter price for item 3: "))
priceFour = float(input("Enter price for item 4: "))
priceFive = float(input("Enter price for item 5: "))

subtotal = priceOne + priceTwo + priceThree + priceFour + priceFive
print("Subtotal: $%.2f" % subtotal)

tax = subtotal * 0.07
print("Tax: $" + str(tax))

total = subtotal + tax
print("Total: $" + str(total))




