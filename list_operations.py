#allowed amount of attempts
attempt = 5
#empty list created
list = []
while 0 < attempt < 6:
    user_input = int(input("Enter your number: "))
    list.append(user_input)
    attempt -= 1
#decrease the attempt by 1 after each loop
print(list)

#below are different trail of list, sorted is the unmodified version
print("Sorted without modify: ", sorted(list))
list.sort()
print("Sorted: ", list)

input2 = int(input("Enter your adding number: "))
list.insert(4, input2)
print("Inserted: ", list)

del list[2]
print("Deleted: ", list)

list.reverse()
print("Reversed: ", list)
