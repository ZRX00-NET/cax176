#set range for all grade
a = range(90, 101)
b = range(80, 90)
c = range(70, 80)
d = range(60, 70)
f = range(0, 60)

#inputs
name = input("What if your name: ")
print("nice to meet you", name)
grade = int(input("what is your grade: "))

#if condition for all grades
if grade in a:
    print("Your grade is: A")
elif grade in b:
    print("Your grade is: B")
elif grade in c:
    print("Your grade is: C")
elif grade in d:
    print("Your grade is: D")
elif grade in f:
    print("Your grade is: D")
else:
    print("Enter a valid grade.")

#conditional lines
if grade in a or grade in b or grade in c:
    print("Great Job!")
elif grade in d or grade in f:
    print("Work harder!")