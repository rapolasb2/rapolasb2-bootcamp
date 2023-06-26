import math

# Created a variable that stores user input for their choice of calculation 
# and converted the input to lower case to avoid confusion over letter capitalisation

print("Investment - to calulate the amount of", end= " ")
print("interest you'll earn on your investment")
print("Bond       - to calulate the amount you'll", end= "")
print(" have to pay on a home loan\n")
choice = input("""Enter either 'investment' or 'bond'
 from the menu above to proceed: """)

type = choice.lower()

# Created a branch of conditional statement that calculates investment value
# based on user inputs of initial investment, interest rate (and type) and time of investment or

if type == "investment":
    amount = int(input("Please enter the amount of money that you are depositing: "))
    interest_rate = int(input("Please enter the interest rate as a number without the percentage sign: ")) / 100
    time = int(input("Please enter the number of years you plan to invest: "))
    interest = input("Please enter whether the interest is 'simple' or 'compound': ")
    interest_type = interest.lower()
    
    if interest_type == "simple":
        investment_value = amount * (1 + interest_rate * time)
        print("Total value of investment after " + str(time), end= " ")
        print("years with simple interest of " + str(interest_rate*100), "%: ", end= " ")
        print(str(investment_value))

    elif interest_type == "compound":
        investment_value = amount * math.pow((1 + interest_rate), time)
        print("Total value of investment after " + str(time), end= " ")
        print("years with compound interest of " + str(interest_rate*100), "%: ", end= " ")
        print(str(investment_value))
    
    else:
        print("Please restart the program and enter a valid interest type")

# Created a branch of conditional statement that calculates monthly repayments
# based on user inputs of value, interest rate and repayment time 

elif type == "bond":
    value = int(input("Please enter the present value of the house: "))
    interest_rate = int(input("Please enter the interest rate as a number without the percentage sign: ")) / 100
    time = int(input("Please enter the number of months you plan to take to repay the bond: "))
    repayment = (interest_rate * value) / (1 - (1 + interest_rate)**(-time))
    print("Each month you will have to repay: " + str(repayment))

else:
    print("Please restart the program and enter a valid calculation type.")
    

