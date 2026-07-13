#user input
input1 = input("Enter first boolean input: ")
input2 = input("Enter second boolean input: ")

#set conditions for input 1
if input1 in ["yes", "True", "true", "Yes", "1", "Y", "y", "t"]:
    input1 = True
elif input1 in ["No", "N", "False", "false", "0", "n","no", "f"]:
    input1 = False

#set condition for input2
if input2 in ["yes", "True", "true", "Yes", "1", "Y", "y"]:
    input2 = True
elif input2 in ["No", "N", "False", "false", "0", "n","no"]:
    input2 = False

#print with the and, or ,not
print("First and Second: ", input1 and input2, "\n", "First or Second: ", input1 or input2, "\n", "Not first: ", not input1)

# trail with bit operators
print(bin(5&3))
print(bin(5^3))
print(bin(5|3))
print(bin(5&~3))
print(bin(5&3<<3))
print(bin(20>>3))