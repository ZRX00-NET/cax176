#create empty definition
ContactList = {}
                
#create first function group to be revocate later
#double layer function is needed since user entry needs to be enter outside the function AddNewContact and group them for cleaner outlook.
def AddContact():
    def AddNewContact(name, Pnumber):
        #make sure the entry is not duplicated
        if name not in ContactList:
            if name.isalpha():
                #update the def list
                ContactList.update({name: Pnumber})
                print("Contact added.")
            else:
                print("Please enter valid name.")
        else:
            print("Do Not Enter Duplicate Entry.")

    #define the input from user
    nameE = input("Please enter contact name: ")
    try:
        PnumberE = int(input("Please enter the phone number: "))
        #revoke the function
        AddNewContact(name = nameE, Pnumber = PnumberE)
    except:
        print("Invalid phone number!")

#create second function group
def ViewAllContact():
    #if the def list is empty
    if len(ContactList) == 0:
        print("Empty Contact List.")
    else:
        #loop and list out the key:value then print
        for name, Pnumber in ContactList.items():
            print("Contact: ", name, Pnumber, end = "\n")


#Create third function group
def search():
    findN = input("Input contact name: ")
    #if user entry is in the def list
    if findN in ContactList:
        #print the according value
        print(ContactList[findN])
    else:
        #if not
        print("Please enter valid name.")


#Create fourth functioni group
def delete():
    #user's entry
    delN = input("Enter the contact name you want to delete: ")
    #if find in the definition list
    if delN in ContactList:
        #del
        del ContactList[delN]
        #confirm deleted with user
        print("Contact deleted.")
    else:
        #if cannot find in the list
        print("Please enter valid name.")


#set condition to always true so the while loop always loop
truth = True

#create while loop
while truth == True:
    #print the user interface
    print("1. Add New Contact", "2. View All Contacts", "3. Search Contact", "4. Delete Contact", "5. Exit", sep = "\n")
    #create input variable the user enter
    choice = int(input("Enter your choice (1-5): "))
    #call the function base on user's choice.
    #only accept entry as integer
    if type(choice) is int:
        if choice == 1:
            AddContact()
        elif choice == 2:
            ViewAllContact()
        elif choice == 3:
            search()
        elif choice == 4:
            delete()
        elif choice == 5:
            exit()
        #if user enter number outside of 1-5
        else:
            print("Please enter number from 1 to 5.")
    #if not integer enter:
    else:
        print("Please enter integer: ")


    
            