# ali_baasil_donuts.py
#
# Our program will ask for the number 
# of plain donuts the customer wants
# and then will ask how many fancy donuts
# they want. From there we will calculate
# the total cost due, based on the price type of each.
#
# Baasil Ali, 0ctober 6, 2022
#

plainDozenPrice = 7.00      #begin by initializing prices to prevent using "magic numbers" later in the code
plainSinglePrice = 0.60     #seperate the prices by plain and fancy for clarity

fancyDozenPrice = 9.00
fancySinglePrice = 0.80

numPlain = int(input("Enter the number of plain donuts you want to buy: "))     #Ask for integer input
numFancy = int(input("Enter the number of fancy donuts you want to buy: "))     #for plain and fancy donuts

pDozen = numPlain // 12     #Use floor division for dozens to get rid of remainders
pSingle = numPlain % 12     #Use % to actually get the remainder and seperate them

fDozen = numFancy // 12
fSingle = numFancy % 12

pCost = (pDozen * plainDozenPrice) + (pSingle * plainSinglePrice)       #Do the math for total plain
fCost = (fDozen * fancyDozenPrice) + (fSingle * fancySinglePrice)       #and fancy costs

total = pCost + fCost       #Add the two costs together to get the total price of all donuts bought

print("Plain donuts: ")
print("\t" + str(pDozen) + " dozen and " + str(pSingle) + " single")        #Print output
print("\tCost: $%.2f" % pCost)

print("Fancy donuts: ")
print("\t" + str(fDozen) + " dozen and " + str(fSingle) + " single")
print("\tCost: $%.2f" % fCost)

print("Total amount due: $%.2f" % total)