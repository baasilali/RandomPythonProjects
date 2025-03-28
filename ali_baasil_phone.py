#This program will display all monetary amounts for the cost of units using two seperate plans. 
#From there, we will notify the user which of the two plans is cheaper.
#We will take input from the user and will specifically ask for the number of units used.

#First, we create a function to ask how many units
def get_units():
    numUnits = int(input("Enter number of units used: "))
    return numUnits

#Next, we create a function that can calculate the cost
def calculate_cost(units, base_cost, base_limit, cost_over_limit):
    cost = base_cost

    if units > base_limit:
        units -= base_limit
        cost += (cost_over_limit * units / 100)

    return cost

#Finally, we will write the main function which calls the two prior functions and actually displays the result
def main():
    units = get_units() 

    if units < 0:
        print("You cannot have negative units.")

    else:
        planOne = format(calculate_cost(units, 9.38, 65, 4.5), '.2f')
        planTwo = format(calculate_cost(units, 8.57, 50, 5.2), '.2f')

        print('Cost for plan 1: $' + planOne)
        print('Cost for plan 2: $' + planTwo)

        if planOne > planTwo:
            print("Plan 2 is cheaper.")

        else:
            print("Plan 1 is cheaper")


if __name__ == '__main__':
    main()