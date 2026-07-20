def getAGrade(gradesT):
    try: 
        total = 0
        for i in gradesT:
            total = total + i
        lenght = len(gradesT)
        return total/lenght
    except ZeroDivisionError:
        print("Must enter numbers.")

grades = 32, 43, 43, 12, 67
result = getAGrade(grades)
print(result)

course_grades = {}

math = 90, 45, 87, 92, 23
result = getAGrade(math)
print(result)

science = 68, 98, 58, 32,98
result = getAGrade(science)
print(result)

history = ()
result = getAGrade(history)
print(result)
