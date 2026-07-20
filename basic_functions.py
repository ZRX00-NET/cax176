# def greet_user(name=""):
#     if name == "":
#         print("Hello! Welcome!")
#     else:
#         print("Hello,", name + "! Welcome!" )

# name = str(input("PLease enter your name: "))
# greet_user(name)
# greet_user()

# def add_two_numbers(a, b):
#     return a + b

# sum = add_two_numbers(2, 7)
# print(sum)

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

result = is_even(4)
print("4 is even:", result)

result = is_even(1)
print("1 is odd:", result)