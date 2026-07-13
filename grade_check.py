name = input("What if your name: ")
print("nice to meet you", name)
grade = int(input("what is your grade: "))


if 90 <= grade <= 100:
    print("Your grade is: A")
elif 80 <= grade <= 89:
    print("Your grade is: B")
elif 70 <= grade <= 79:
    print("Your grade is: C")
elif 60 <= grade <= 69:
    print("Your grade is: D")
elif 0 <= grade <= 59:
    print("Your grade is: D")
else:
    print("Enter a valid grade.")

