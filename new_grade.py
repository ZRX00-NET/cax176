name = input("What if your name: ")
print("nice to meet you", name)
grade = int(input("what is your grade: "))

a = [90, 100]
b = [80, 89]
c = [70, 79]
d = [60, 69]
f = [0, 59]

if grade == a:
    print("Your grade is: A")
elif grade == b:
    print("Your grade is: B")
elif grade == c:
    print("Your grade is: C")
elif grade == d:
    print("Your grade is: D")
elif grade == f:
    print("Your grade is: D")
else:
    print("Enter a valid grade.")

if grade == a or grade == b or grade == c:
    print("Great Job!")
elif grade == d or grade == f:
    print("Work harder!")