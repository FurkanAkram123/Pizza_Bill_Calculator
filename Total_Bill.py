print("Welcome to Pizza Bill Calculator! ")

# Define the size variable.
# Size vs price of pizza:
# Small pizza: $15
# Medium pizza: $20
# Large pizza: $25

size = ""

# Define the Pepperoni variable for extra pepperoni
# Pepperoni: $3

Pepperoni = ""

# Define the Extra cheese variable for extra pepperoni
# extra cheese: $1
extra_cheese = ""

# Define the bill variable
bill = 0

if bill == 0:
    # What size does the customer want?
    size = input("What size do you want? ")

    if size == "Large":
        bill += 25

    elif size == "Medium":
        bill += 20

    elif size == "Small":
        bill += 15
    else:
        print("invalid entry please try again")

    # Does the customer want pepperoni?
    if size == "Large" or size == "Small" or size == "Medium":
        Pepperoni = input("Do you want pepperoni on the pizza? Type 'y' for yes and 'n' for no: ")
        if Pepperoni == "y":
            bill += 3

    # Does the customer want extra cheese"
    if size == "Large" or size == "Small" or size == "Medium":
        extra_cheese = input("Do you want extra cheese on the pizza? Type 'y' for yes and 'n' for no: ")
        if extra_cheese == "y":
            bill += 1

    # Print the final bill
    print(f"your total bill is ${bill} :)")
    bill = 0
