# Variables and Calculations - Monthly Loan Payment
# Baasil Ali
# 09 / 20 / 22

#Take initial loan input (P)
loan = float(input("Enter amount of loan: $")) 
#Take interest rate input (as a percent)
intRate = float(input("Enter annual interest rate as a percent: "))
#Take total years of loan input
years = int(input("Enter number of years for the loan: "))

#create varaibles to make a digestible equation
r = (intRate / 100) / 12.0
n = years * 12.0
subF = ((1 + r) ** n)

#calculate monthly payment
mPay = loan * ((r * subF) / (subF - 1))

print("Your monthly payment is $%.2f" % mPay)
