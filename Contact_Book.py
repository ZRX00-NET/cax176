ContactList = {}

def AddContact():
    def AddNewContact(name, Pnumber):
        #name = input("Please enter contact name: ")
        #Pnumber = input("Please enter the phone number: ")
        if name not in ContactList:
            ContactList.update({name: Pnumber})
            print("Contact added.")
        else:
            print("Do Not Enter Duplicate Entry.")

    nameE = input("Please enter contact name: ")
    PnumberE = input("Please enter the phone number: ")
    AddNewContact(name = nameE, Pnumber = PnumberE)


def ViewAllContact():
    if len(ContactList) == 0:
        print("Empty Contact List.")
    else:
        for name, Pnumber in ContactList.items():
            print("Contact: ", name, Pnumber, end = "\n")
                    
                    

AddContact()
ViewAllContact()

    
            