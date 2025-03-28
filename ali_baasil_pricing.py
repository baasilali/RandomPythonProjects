#Baasil Ali
# 12 / 14 / 2022
#
# This program will ask for the rpice of the product and the 
# quantity ordered. It will then calculate and output, proper labeled,
# the price before discount, the amount of discount (if any), and the 
# total amount of purchase after the discount.

def main():
    price = float(input("Enter the price of the product: $"))
    quanity = int(input("Enter the quantity: "))

    prePrice = price * quanity
    discount = 0.0

    if quanity < 10:
        discount = 0.0
    elif quanity <= 19:
        discount = 0.1
    elif quanity <= 49:
        discount = 0.2
    elif quanity <= 99:
        discount = 0.25
    else:
        discount = 0.3

    netDiscount = discount * prePrice
    totalPrice = prePrice - netDiscount

    print("Total price before discount: $%.2f" % prePrice)
    print("Amount of discount: $%.2f" % netDiscount)
    print("Total price after discount: $%.2f" % totalPrice)


main()