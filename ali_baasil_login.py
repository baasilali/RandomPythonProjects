# Baasil Ali
# 12 / 14 / 2022
#
# In this program we prompt the user for a first name, last name
# and 7 digit ID. The program will then create a login name according
# to the following algorith given:
#
# 1. Get the first two characters of the first name. Convert these characters to lowercase.
# 2. Get the first two characters of the last name. Convert these characters to lowercase.
# 3. Get the last three digits of the ID number.
# 4. Concatenate the three strings above to generate the login name.
#

# Define the function get_login_name that accepts the first name, last name, and ID number as arguments
def get_login_name(first_name, last_name, id_number):
    # Get the first two characters of the first name and convert to lowercase
    first_name_initials = first_name[:2].lower()

    # Get the first two characters of the last name and convert to lowercase
    last_name_initials = last_name[:2].lower()

    # Get the last three digits of the ID number
    id_number_last_digits = id_number[-3:]

    # Concatenate the strings to generate the login name
    login_name = first_name_initials + last_name_initials + id_number_last_digits

    # Return the login name
    return login_name

# Get the first name, last name, and ID number from the user
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
id_number = input("Please enter a 7 digit ID number: ")

# Generate the login name using the function get_login_name
login_name = get_login_name(first_name, last_name, id_number)

# Display the login name
print("Your login is:", login_name)