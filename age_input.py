Set = True

while Set:
    age = input("What is your age: ")
    try:
        int(age)
        print("Success! Your age is: ")
    except ValueError:
        print("Error: That is not a valid number!")
