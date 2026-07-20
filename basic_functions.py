#define function and assign parameter to empty string
def greet_user(name=""):
    #if user enter nothing
    if name == "":
        print("Hello! Welcome!")
        #if user entered name
    else:
        print("Hello,", name + "! Welcome!" )

#trigger input from user
name = str(input("PLease enter your name: "))
#invocate function with the input
greet_user(name)
#invocate function with no input
greet_user()

#create function
def add_two_numbers(a, b):
    #return with expression for sum
    return a + b

#assign the result of the function to variable
sum = add_two_numbers(2, 7)
print(sum)

#create function
def is_even(num):
    #if even
    if num % 2 == 0:
        return True
    #if not
    else:
        return False

#test as 4
result = is_even(4)
print("4 is even:", result)
#test as 1
result = is_even(1)
print("1 is even:", result)