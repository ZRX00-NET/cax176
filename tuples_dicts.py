# months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",)
# print(months[0], months[-1])
# try:
#     months[0] = "NewMonth"
# except Exception as e:
#     print("Tuples are immutable, error: ", e)

students = {"Amy":100, "John":1, "Jess": 87}
students.update({"Ryan":96})
print(students)
students["Jess"] = 90
print("Jess:", students.get("Jess"))

for name, value in students.items():
    print(name, ":", value)