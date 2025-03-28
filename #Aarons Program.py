#Aarons Program

totalGallons = 0.0
totalMiles = 0
totalMpg = 0.0



while True:

    gallons = float(input("Enter the gallons used (any negative number to end): "))

    if gallons >= 0:

        miles = int(input("Enter the miles driven: "))
        
        totalMiles = totalMiles + miles
        totalGallons = totalGallons + gallons

        mpg = miles / gallons

        print("The miles per gallon for this tank was %.6f" % mpg)

    else:
        
        totalMpg = totalMiles / totalGallons

        print("The overall average miles/gallon was %.6f" % totalMpg)

        False

        break







        




    




    













