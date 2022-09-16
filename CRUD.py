#(Enter Numbers to choice what you want....:)
#"""Enter 1 for add 
#Enter 2 for delete 
#Enter 3 for update 
#Enter 0 to delete"""
names = []

def addName(name):
    name = input("Enter a name: ")
    names.append(name)
    return

def deleteName(name):
    name = input(" Please enter the user's Name:")
    if name in names:
        index = names.index(name)
        names.pop(index)
        print(" Deleted successfully ")
        print(names)
    else:
        print(" No deleted user found !")
        print(names)
    return

def updateName(name):
    name = input(" Please enter the user's Name:")

    if name in names:
        index = names.index(name)
        names[index]= input(" Please enter the user's name :")
        print(" Updated successfully ")
        print(names)
    else:
        print(" No update were found !")
        print(names)
    return

while True: 
    type =int(input("""
        Enter 1 for add 
        Enter 2 for delete 
        Enter 3 for update 
        Enter 4 to Read
        Enter 0 to Exit
         Enter Your Choice: 
        """)) 
        
    if type == 1:
        addName(names)
        print("Added Successfully....")
    elif type==2:
        deleteName(names)
        print("Deleted Successfully....")
    elif type == 3:
         updateName(names)
         print("Update Successfully....")
    elif type == 4:
        print(names)
    elif type == 0:
        print("Re-try")
        break
    else:
        print("Sorry! Have been Entered Invalid Number....")


