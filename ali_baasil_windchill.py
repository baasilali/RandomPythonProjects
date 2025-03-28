# Ali_Baasil_windchill.py
# Varaibles and Calculations: Wind Chill
# Baasil Ali
# 09 / 20 / 22

t = float(input("Enter temperature in degrees Celsius: ")) #Takes input for T (temperature)
windV = float(input("Enter wind velocity in kilometers/hour: ")) #Takes input for V (velocity)

#Calculate wind chill using given formula
windChill = 13.12 + (0.6215 * t) - (11.37 * (windV ** 0.16)) + (0.3965 * t * (windV ** 0.16))

#Display output
print("The wind chill temperature in degrees Celsius is %.3f" % windChill)