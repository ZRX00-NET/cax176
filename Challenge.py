age = int(input("What is your age: "))

while type(age) != int:
    print(input("Enter age number: "))
    break

if age < 18:
    print("Damn no!")
elif 18 <= age <= 20:
    print("Come in, but no drinks for you.")
else:
    print("Welcome in! Drink drink drink.")
    