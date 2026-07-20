#create the tuples include the months
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",)
#print the first and the last month
print(months[0], months[-1])
#tuples are unchangeable, but use try & except as requested to avoid crash as we are trying to change months[0]
try:
    months[0] = "NewMonth"
except Exception as e:
    print("Tuples are immutable, error: ", e)

#create the dictionary with its keys and values
students = {"Amy":100, "John":1, "Jess": 87}
#add new key and value
students.update({"Ryan":96})
#print all the keys and value within the list
print(students)
#update the value of key Jess
students["Jess"] = 90
print("Jess:", students.get("Jess"))

#this loop through the dictionary and print out all the key and value
for name, value in students.items():
    print(name, ":", value)