# This program gives users access to an investment calculator and a home loan repayment calculator

import math

print("Choose ether 'investment' or 'bond' from the menu below to proceed:")
print("\ninvestment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

while True:
    user_choice = input("Enter your choice here: ")
    # Convert user input to lower case in the case of user entering strings of different cases
    user_choice = user_choice.lower()


    if user_choice == "investment":
        principal = float(input("Enter the amount of money being deposited: "))
        i_rate = float(input("Enter the interest rate as a percentage without the % sign: "))
        years = int(input("Enter the number of years you plan on investing for: "))

        while True:
            interest = input("Do you want simple interest or coumpound interest? For simple interest, type simple. For compound interest, type compound: ")

            interest = interest.lower()

            if interest == "simple":
                total_amount = principal*(1 + (i_rate/100)*years)
                break

            elif interest == "compound":
                total_amount = principal*math.pow((1+(i_rate/100)),years)
                break

            else:
                print("Error! You have entered the wrong option. Please enter simple or compound")

                continue
        
        print("The total amount after {} years is R{:0,.2f}".format(years, total_amount))

        break

    elif user_choice == "bond":
        p_value = float(input("Enter the present value of the house: "))
        i_rate = float(input("Enter the annual interest rate as a percentage without the % sign: "))
        months = int(input("Enter the number of months you plan to take to repay the bond: "))

        amount = ((i_rate/1200)*p_value)/(1 - math.pow((1 + (i_rate/1200)),-months))

        print("The amount of money to be repaid each month is R{:0,.2f}".format(amount))

        break

    else:
        print("\nError! You have entered the wrong option. Please select investment or bond")

        continue
