#define addition function
def add(a, b):
    return a + b

#subtraction function
def subtract(a, b):
    return a - b

#multiplication function
def multiply(a ,b):
    return a * b
#division function
def divide(a, b):
    return a / b

#main logic function
def calculate(a, b, op):
    #use try & except to avoid error such as zero as divitor etc
    try: 
        #here uses if and elif to set condidtion to call different functions
        if op == "+":
            print(add(a, b))
        elif op == "-":
            print(subtract(a, b))
        elif op == "*":
            print(multiply(a ,b))
        elif op == "/":
            print(divide(a, b))
        #else set to do what happen when user enter other op
        else:
            print("Please enter +, -, *, or /.")
    except Exception as e:
        print(e, "Encountered Error.")

#use try and except to make sure user enter int for both inputs
try:
    a = int(input("Please enter your first number: "))
except Exception as error:
    print(error, "Please enter a int")
    exit()
try:
    b = int(input("Please enter your second number: "))
except Exception as error:
    print(error, "Please enter a int")
    exit()

#no need to user try & except since we already did in the calculate function
op = str(input("Please enter your operator: "))
#invocate the main function to start the calculation
calculate(a, b, op)
