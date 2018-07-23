# ChangeMachine.py
#
# Description: This Python program calculates the change to be given back to a customer when
#              s/he makes a purchase such that it maximizes the number of $10 bills, then $5 bills,
#              then $2 coin (toonies) etc.. all the way down to $0.05 coin (nickels)
#              given back to the customer.
#
# Anne Lavergne
# Modified on January 2017

# Set up our money variables
centValueOfTenDollarBill = 1000
centValueOfFiveDollarBill = 500
centValueOfToonie = 200
centValueOfLoonie = 100
centValueOfQuarter = 25
centValueOfDime = 10
centValueOfNickel = 5

# Set up the variable purchaseTotal by asking the user for the total of purchase   
purchaseTotal = float(input("Please, enter the total of the purchase: "))
# Set up the variable moneyPaid by asking the user for the money the customer has given to pay for the purchase
moneyPaid = float(input("Please, enter the amount given by the customer: "))
                            
# Figure out the change
change = moneyPaid - purchaseTotal

# Echo input data to user
print("""The total of the purchase is $%0.2f.
The customer paid $%0.2f. 
The cashier gives $%0.2f back to the customer in the following fashion: """
      %(purchaseTotal, moneyPaid, change)) 

#Convert dollars into cents to facilitate the computation
purchaseTotalInCents = round(purchaseTotal * 100)
moneyPaidInCents = round(moneyPaid * 100)
changeInCents = round(change * 100)

# Determine # of $10 to be given back as part of the change
numberOfTenDollarBills = changeInCents // centValueOfTenDollarBill
changeInCents %= centValueOfTenDollarBill

# Determine # of $5 to be given back as part of the change
numberOfFiveDollarBills = changeInCents // centValueOfFiveDollarBill
changeInCents %= centValueOfFiveDollarBill

# Determine # of $2 (toonies) to be given back as part of the change
numberOfToonieCoins = changeInCents // centValueOfToonie
changeInCents %= centValueOfToonie

# Determine # of $1 (loonies) to be given back as part of the change
numberOfLoonieCoins = changeInCents // centValueOfToonie
changeInCents %= centValueOfLoonie

# Determine # of $0.25 (quarters) to be given back as part of the change
numberOfQuarterCoins = changeInCents // centValueOfQuarter
changeInCents %= centValueOfQuarter

# Determine # of $0.10 (dimes) to be given back as part of the change
numberOfDimeCoins = changeInCents // centValueOfDime  
changeInCents %= centValueOfDime

# At this point, changeInCents can either be
# 5 -> 1 x $0.05 (nickels) or
# 0 -> 0 x $0.05 (nickels)
numberOfNickelCoins = changeInCents // centValueOfNickel

# Output the result: change cashier needs to give back to customer
print("\t%i x $10.00" %numberOfTenDollarBills)
print("\t%i x $ 5.00" %numberOfFiveDollarBills)
print("\t%i x $ 2.00" %numberOfToonieCoins)
print("\t%i x $ 1.00" %numberOfLoonieCoins)  
print("\t%i x $ 0.25" %numberOfQuarterCoins)
print("\t%i x $ 0.10" %numberOfDimeCoins)
print("\t%i x $ 0.05" %numberOfNickelCoins)

# Indicates the end of execution
print("----\n")
