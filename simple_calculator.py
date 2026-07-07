Var = float(input("Enter your first number: "))

Var2 = float(input("Enter your second number: "))

operation = input("Choose an operation: +, -, *, /: ")

if operation == "+":
    addition = Var + Var2
    print(Var, "+", Var2, "=", addition)
elif operation == "-":
    subtraction = Var - Var2
    print(Var, "-", Var2, "=", subtraction)
elif operation == "*":
    multiplication = Var * Var2
    print(Var, "*", Var2, "=", multiplication)
elif operation == "/":
    division = Var / Var2
    print(Var, "/", Var2, "=", division)
else:
    print("Choose the listed operator please")