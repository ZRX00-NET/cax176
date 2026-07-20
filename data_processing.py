#create the function that performs the operation
def getAGrade(gradesT):
    #uses try & except to avoid empty tuples
    try: 
        #define what is total for the initial calculation
        total = 0
        # for loop to loop through the value in tuple gradesT
        for i in gradesT:
            #the addition
            total = total + i
        #need to know the amount of value in the tuples
        lenght = len(gradesT)
        #the average expression
        return total/lenght
    except ZeroDivisionError:
        print("Must enter numbers.")

#define the value in tuples for math
math = 90, 45, 87, 92, 23

#define the value in tuples for science
science = 68, 98, 58, 32,98

#define the value in tuples for history
history = ()

#create the dictionary as requested
course_grades = {"Math":math, "Science": science, "History": history}

#loop through all the keys in dictionary
for subject in course_grades.keys():
    #se if and elif to define what function to call under certain condition
    if subject == "Math":
        result = getAGrade(math)
        print("The average grade for Math is: ", result)
    elif subject == "Science":
        result = getAGrade(science)
        print("The average grade for Math is: ", result)
    elif subject == "History":
        result = getAGrade(history)
        print("The average grade for Math is: ", result)
