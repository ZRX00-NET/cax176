def calculator(originalP):
    discountR = 0.10
    finalP = originalP - (originalP * discountR)
    #return finalP

originalP = int(input("What is the original price: "))

print(calculator(originalP))
