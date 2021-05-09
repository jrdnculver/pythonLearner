import csv

contactNames = []
contactNumbers = []
file = "phoneBook.csv"


def usingPhoneBook(file):
    numChoose = intro(file)

    if numChoose == 1:
        printContacts(
            file)
    elif numChoose == 2:
        addContact(file)
    elif numChoose == 3:
        searching = searchContact(file)
        searchSearch(searching)
    elif numChoose == 4:
        lines, contactDel, field = deleteContact()
        i, confirmDel = deleteSearch(contactDel)
        if confirmDel == True:
            deleting(contactDel, field, lines, i)
            writingLines(lines, file)
    else:
        print("Thanks for using phonebook!")
        exit()
    menuReturn()


def intro(file):

    print("\n")
    print("1. Display Your Contacts")
    print("2. Create a New Contact")
    print("3. Check an Entry")
    print("4. Delete an Entry")
    print("5. Exit Program\n")
    print("The following numbers allow you to perform various task within the phone book")
    while True:
        try:
            numChoose = int(input(
                "What would you like to do, press the corresponding value to perform operation: "))
            break
        except:
            print("That is not a valid option. Try Again!")

    return numChoose


def printContacts(file):
    print(file)
    with open(file, "r") as dataFile:
        reader = csv.reader(dataFile)
        for line in reader:
            if line != []:
                print(f"\nName: {line[0]}\nNumber: {line[1]}\n")


def addContact(file):
    print("\nYou can add a New Contact")
    while True:
        firstName = input("\nWhat is the first Name: ")
        firstName = firstName.title()
        lastName = input("\nWhat is the last Name: ")
        lastName = lastName.title()
        checking = checkingInput()
        if checking == "Y":
            break
    while True:
        phoneNum = input("\nEnter Number (10 Characters Required!): ")
        if len(phoneNum) != 10:
            print("\nThat's an invalid number.  Try Again!")
        else:
            break

    phoneNum = f"({phoneNum[0:3]}){phoneNum[3:6]}-{phoneNum[6:10]}"
    fullName = firstName + " " + lastName

    with open(file, "a") as contactBook:
        contactBook.write(f"\n{fullName},{phoneNum}")
    print("Your contact successfully saved.")


def searchContact(file):
    lines = []
    searching = []

    contactF = input("\nWhat is the first name?: ")
    contactF = contactF.title()
    contactL = input("\nWhat is the last name?: ")
    contactL = contactL.title()
    print()
    with open(file, "r") as dataFile:
        reader = csv.reader(dataFile)
        for line in reader:
            if line != []:
                lines.append(line)
            for field in line:
                splitting = (field.split(" "))
                if splitting[0][0] == contactF[0] and splitting[1][0] == contactL[0] and len(splitting) > 1:
                    search = [field, line[1]]

                    searching.append(search)
    return searching


def deleteContact():
    lines = []
    contactDel = []

    contactF = input("\nType the first name: ")
    contactF = contactF.title()
    contactL = input("\nType the last name: ")
    contactL = contactL.title()
    with open("phoneBook.csv", "r") as dataFile:
        reader = csv.reader(dataFile)
        for line in reader:
            if line != []:
                lines.append(line)
            for field in line:
                splitting = (field.split(" "))
                if (splitting[0][0] == contactF[0]) and (splitting[1][0] == contactL[0]) and len(splitting) > 1:
                    delete = [field, line[1]]
                    contactDel.append(delete)

    return lines, contactDel, field


def searchSearch(searching):
    i = 0
    while True:
        if searching == []:
            print("There are no valid names!")
            break
        print(f"\nName: {searching[i][0]}\nNumber: {searching[i][1]}\n")
        i += 1
        checking = checkingInput()
        if checking[0] == "Y":
            break

        if i == len(searching):
            print("\nThere are no other valid names!")
            break

    return searching


def deleteSearch(contactDel):
    i = 0
    while True:
        if contactDel == []:
            print("There are no valid names!")
            confirmDel = False
            break
        print(f"\nName: {contactDel[i][0]}\nNumber: {contactDel[i][1]}")
        checking = checkingInput()
        if checking[0] == "Y":
            confirmDel = True
            break
        if i == len(contactDel) - 1:
            print("\nThere are no other valid names!")
            confirmDel = False
            break
        i += 1

    return i, confirmDel


def deleting(contactDel, field, lines, i):
    for line in lines:
        if contactDel[i] == line:
            lines.remove(contactDel[i])
            print("\nThis contact has been deleted!")

    return lines


def writingLines(lines, file):
    with open(file, "w") as writerFile:
        writer = csv.writer(writerFile)
        writer.writerows(lines)


def menuReturn():
    response = input("\nReturn to main menu? Enter (Y or N): ")

    if response.upper() == "Y":
        usingPhoneBook(file)

    elif response.upper() == "N":
        pass

    else:
        print("\nDid not understand. Please try again!")
        menuReturn()


def createCSV(file):
    f = open(file, "w")
    f.close()

    return file


def checkingInput():
    checking = input("\nIs this correct? (Y or N): ")
    checking = checking.upper()

    return checking


createCSV(file)
usingPhoneBook(file)
