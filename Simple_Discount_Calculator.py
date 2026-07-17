def calculator(originalP):
    #set default discount rate as requested
    discountR = 0.10
    #expression
    finalP = originalP - (originalP * discountR)
    #return the result so the invoke line won't be empty.
    return finalP

#Have user input the price
originalP = float(input("What is the original price: "))

#invoke/call the function
print(calculator(originalP))
