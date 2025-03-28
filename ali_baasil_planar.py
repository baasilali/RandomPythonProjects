#Baasil Ali
#12 / 14 / 2022
# Thid program uses functions to calulate distance

def distance(x, y, x1, y1):
    return format(((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5, '.2f')

def block_distance(x, y, x1, y1):
    return format(abs(x - x1) + abs(y - y1), '.2f')

def main():
    x = float(input("Enter x of first point: "))
    y = float(input("Enter y of first point: "))
    x1 = float(input("Enter x of second point: "))
    y1 = float(input("Enter y of second point: "))

    print("Pythagoren distance between the 2 points is " + str(distance(x, y, x1, y1)))
    print("City Block distance between the 2 points is " + str(block_distance(x, y, x1, y1)))

main()