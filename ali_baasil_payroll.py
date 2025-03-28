#Baasil Ali
#12 / 14 / 2022
#
# Calculate an individuals payroll based on the number of hours worked
# and the hourly rate. The output should give the number of wages.

def wages(hours, rate):
    # Calculate the total wages for the week
    
    if (hours > 40):
        return (hours * rate) + ((hours - 40) * (rate * 1.5))
    else:
        return hours * rate

def main():
    # Input the number of hours worked and the hourly rate
    hours = float(input("Enter the number of hours worked in the week: "))
    rate = float(input("Enter the hourly rate: "))

    # Calculate the total wages
    total_wages = wages(hours, rate)

    # Print the total wages, with a dollar sign and exactly two digits after the decimal point
    print("Total wages for the week: $%.2f" % total_wages)

# Call the main function
main()
