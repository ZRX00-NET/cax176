ContactList = {}

def AddNewContact(name, Pnumber):
    #name = input("Please enter contact name: ")
    #Pnumber = input("Please enter the phone number: ")
    if name not in ContactList and name not in ContactList:
        ContactList.update({name: Pnumber})
        print("Contact added.")
    else:
        print("Do Not Enter Duplicate Entry.")

nameE = input("Please enter contact name: ")
PnumberE = input("Please enter the phone number: ")
AddNewContact(name = nameE, Pnumber = PnumberE)

    
            