import tkinter as tk
import random as rnd
from tkinter.constants import PROJECTING
import sys


class Program:

    def tierOne(self):

        print("I am tier One")
        gui.rootProperties()
        gui.rootLabels()
        gui.rootEntries()
        gui.rootButtons()

        gui.root.mainloop()

    def tierTwo(self):

        print("I am tier Two")
        gui.rootSignUpFrame()
        gui.signUpLabels()
        gui.signUpEntries()
        gui.signUpButtons()

        gui.root.mainloop()


class Login:

    def __init__(self):

        self.UserName = ""
        self.Password = ""

    def setUserName(self):

        gui.setUserName()
        self.UserName = gui.getUserName()
        return self.UserName

    def setPassword(self):

        gui.setPassword()
        self.Password = gui.getPassword()
        return self.Password

    def getUserName(self):

        return self.UserName

    def getPassword(self):

        return self.Password

    def setCreateUserName(self):

        gui.setCreateUserName()
        self.CreateUserName = gui.getCreateUserName()
        return self.CreateUserName

    def setCreatePassword(self):

        gui.setCreatePassword()
        self.CreatePassword = gui.getCreatePassword()
        return self.CreatePassword

    def getCreateUserName(self):

        return self.CreateUserName

    def getCreatePassword(self):

        return self.CreatePassword

    def getLogin(self):

        self.setUserName()
        self.setPassword()

    def createLogin(self):
        self.setCreateUserName()
        self.setCreatePassword()


class Gui():

    def __init__(self, userName="", password="", access="NO ACCESS"):
        self.UserName = userName
        self.Password = password
        self.access = access
        self.root = tk.Tk()

    # Will set UserName for Login
    def setUserName(self):

        self.UserName = self.entryUserName.get()

    # WIll set Password for Login
    def setPassword(self):

        self.Password = self.entryPassword.get()

    # Will getUserName for Login
    def getUserName(self):

        return self.UserName

    # Will get Password for Login
    def getPassword(self):

        return self.Password

    # WIll set UserDefined UserName for sign up
    def setCreateUserName(self):
        self.CreateUserName = self.suEntryUserName.get()

    # WIll set UserDefined Password for sign up
    def setCreatePassword(self):
        self.CreatePassword = self.suEntryPassword.get()

    # WIll get UserDefined Login for sign up
    def getCreateUserName(self):
        return self.CreateUserName

    # Will get UserDefined Login for sign up
    def getCreatePassword(self):
        return self.CreatePassword

    # Root window properties
    def rootProperties(self):

        self.root.configure(background="Blue")
        self.root.geometry("500x500")
        self.root.title("LoginSystem")
        self.root.resizable(width=0, height=0)

    # Will create and post labels to root window
    def rootLabels(self):

        self.labelHeader = tk.Label(
            self.root, background="black", foreground="blue", text="PLEASE LOGIN", font=("Times New Roman", 20))
        self.labelHeader.place(relx=.5, rely=.1, anchor="center")

        self.labelUserName = tk.Label(
            self.root, background="black", foreground="blue", text="UserName: ", font=("Courier New", 14))
        self.labelUserName.place(relx=.2, rely=.3, anchor="center")

        self.labelUserName = tk.Label(
            self.root, background="black", foreground="blue", text="Password: ", font=("Courier New", 14))
        self.labelUserName.place(relx=.2, rely=.4, anchor="center")

        self.labelAccess = tk.Label(
            self.root, background="black", foreground="blue", text=self.access, font=("Courier New", 14))
        self.labelAccess.place(relx=.5, rely=.9, anchor="center", width=450)

    # Will create and post entries to root window
    def rootEntries(self):

        self.entryUserName = tk.Entry(
            self.root, background="black", foreground="blue")
        self.entryUserName.place(
            relx=.4, rely=.3, anchor="w", width=190, height=28)

        self.entryPassword = tk.Entry(
            self.root, background="black", foreground="blue")
        self.entryPassword.place(
            relx=.4, rely=.4, anchor="w", width=190, height=28)

    # Will create and post buttons to root window
    def rootButtons(self):

        self.buttonLogin = tk.Button(
            self.root, background="black", foreground="blue", text="Login", command=lambda: [sys.authentification(), pro.tierOne()])
        self.buttonLogin.place(
            relx=.7, rely=.7, anchor="center", width=80, height=45)

        self.buttonLogin = tk.Button(
            self.root, background="black", foreground="blue", text="Sign Up", command=pro.tierTwo)
        self.buttonLogin.place(
            relx=.3, rely=.7, anchor="center", width=80, height=45)

    # Create a frame for sign up window
    def rootSignUpFrame(self):
        self.frameSignUp = tk.Frame(self.root, background="black")
        self.frameSignUp.place(width=500, height=500)

    # Will create and post labels to sign up frame window
    def signUpLabels(self):

        self.suLabelHeader = tk.Label(
            self.frameSignUp, background="black", foreground="blue", text="PLEASE SIGN UP", font=("Times New Roman", 20))
        self.suLabelHeader.place(relx=.5, rely=.1, anchor="center")

        self.suLabelUserName = tk.Label(
            self.frameSignUp, background="black", foreground="blue", text="UserName: ", font=("Courier New", 14))
        self.suLabelUserName.place(relx=.2, rely=.3, anchor="center")

        self.suLabelUserName = tk.Label(
            self.frameSignUp, background="black", foreground="blue", text="Password: ", font=("Courier New", 14))
        self.suLabelUserName.place(relx=.2, rely=.4, anchor="center")

        self.sulabelAccess = tk.Label(
            self.frameSignUp, background="black", foreground="blue", text=self.access, font=("Courier New", 14))
        self.sulabelAccess.place(relx=.5, rely=.9, anchor="center", width=450)

    # Will create and post entries to sign up frame window
    def signUpEntries(self):

        self.suEntryUserName = tk.Entry(
            self.frameSignUp, background="black", foreground="blue")
        self.suEntryUserName.place(
            relx=.4, rely=.3, anchor="w", width=190, height=28)

        self.suEntryPassword = tk.Entry(
            self.frameSignUp, background="black", foreground="blue")
        self.suEntryPassword.place(
            relx=.4, rely=.4, anchor="w", width=190, height=28)

    # Will create and post buttons to sign up frame window
    def signUpButtons(self):

        self.suButtonLogin = tk.Button(
            self.frameSignUp, background="black", foreground="blue", text="Create", command=lambda: [sys.createNewUser(), self.frameSignUp.destroy(), pro.tierTwo()])
        self.suButtonLogin.place(
            relx=.7, rely=.7, anchor="center", width=80, height=45)

        self.suReturnToMenu = tk.Button(
            self.frameSignUp, background="black", foreground="blue", text="Menu", command=lambda: [self.frameSignUp.destroy(), pro.tierOne()])
        self.suReturnToMenu.place(
            relx=.3, rely=.7, anchor="center", width=80, height=45)


class GeneratePassword:

    def __init__(self):

        self.__upperCharacter = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".upper().split(",")
        self.__lowerCharacter = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(
            ",")
        self.__integer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__symbol = "!, @,#,$,%,^,&,*,_,-,+,=".split(",")
        self.__password = ""
        self.errorMessage = "Invalid Username/Password"

    # Getters and Setters

    def setUpperCharacter(self):

        self.UpperCharacter = self.__upperCharacter

    def setLowerCharacter(self):

        self.LowerCharacter = self.__lowerCharacter

    def setInteger(self):

        self.Integer = self.__integer

    def setSymbol(self):

        self.Symbol = self.__symbol

    def setPassword(self):

        self.Password = self.__password

    def getUpperCharacter(self):

        return self.UpperCharacter

    def getLowerCharacter(self):

        return self.LowerCharacter

    def getInteger(self):

        return self.Integer

    def getSymbol(self):

        return self.Symbol

    def getPassword(self):

        return self.Password

    # Will return an uppercase letter if called.

    def generateUpper(self):

        try:

            randomNumber = rnd.randint(0, len(self.__upperCharacter) - 1)
            self.__password = self.__password + \
                self.__upperCharacter[randomNumber]

        except:

            print(self.errorMessage)

    # Will return a lowercase letter if called.

    def generateLower(self):

        try:

            randomNumber = rnd.randint(0, len(self.__lowerCharacter) - 1)
            self.__password = self.__password + \
                self.__lowerCharacter[randomNumber]

        except:

            print(self.errorMessage)

    # Will return an integer letter if called.

    def generateInteger(self):

        try:

            randomNumber = rnd.randint(0, len(self.__integer) - 1)
            self.__password = self.__password + \
                str(self.__integer[randomNumber])

        except:

            print(self.errorMessage)
            gui.access = self.errorMessage

    # Will return a symbol letter if called.

    def generateSymbol(self):

        try:

            randomNumber = rnd.randint(0, len(self.__symbol) - 1)
            self.__password = self.__password + self.__symbol[randomNumber]

        except:

            print(self.errorMessage)
            gui.access = self.errorMessage

    # Will loop through and call functions to generate password of 10 characters.

    def createPassword(self):

        i = 0
        while i < 10:

            randomNumber = rnd.randint(0, 4)

            if randomNumber == 0:
                self.generateUpper()
            elif randomNumber == 1:
                self.generateLower()
            elif randomNumber == 2:
                self.generateInteger()
            else:
                self.generateSymbol()

            i += 1
        self.setPassword()

    # Will shuffle the final result password to promote more randomness with outcome.

    def shufflePassword(self):

        passwordShuffle = [x for x in self.__password]
        rnd.shuffle(passwordShuffle)
        self.__password = "".join(passwordShuffle)
        self.setPassword()


class SystemAccess:

    def __init__(self, maxLoginAttempts=3):

        self.Database = {}
        self.loginAttempts = 0
        self.maxLogins = maxLoginAttempts
        self.maxLogError = "You have too many attempted logins!"
        self.errorMessage = "Invalid Username/Password"
        self.userMessage = "User created Successfully"
        self.userFail = "That UserName already exist!"

    def accessGranted(self):

        return "You've Gained Access"

    def maxLoginError(self):

        try:
            if self.loginAttempts >= 3:
                raise Exception
        except:

            print(self.maxLogError)
            gui.access = self.maxLogError

    def createNewUser(self):
        log.createLogin()

        doesExist = (log.CreateUserName in self.Database)
        print(doesExist)
        try:
            if log.CreateUserName != "" and log.CreatePassword != "":
                if doesExist == False:
                    self.Database[log.CreateUserName] = log.CreatePassword
                    gui.access = self.userMessage
                else:
                    raise Exception
        except:
            gui.access = self.userFail

    def authentification(self):
        log.getLogin()

        while self.loginAttempts <= 3:
            if self.loginAttempts >= 3:
                gui.access = self.maxLogError
                exit()
            try:
                if log.UserName != "" and log.Password != "":
                    if self.Database == {}:
                        self.loginAttempts += 1
                        self.maxLoginError()
                        gui.access = self.errorMessage
                        break
                    elif self.Database[log.UserName] == "":
                        self.loginAttempts += 1
                        self.maxLoginError()
                        gui.access = self.errorMessage
                        break
                    elif self.Database[log.UserName] == log.Password:
                        gui.access = self.accessGranted()
                        break
                    else:
                        print("hello")
                        self.loginAttempts += 1
                        self.maxLoginError()
                        gui.access = self.errorMessage
                        break

                else:
                    self.loginAttempts += 1
                    self.maxLoginError()
                    print(self.errorMessage)
                    break

            except:
                print(self.errorMessage)


if __name__ == "__main__":
    gui = Gui()
    log = Login()
    genPass = GeneratePassword()
    sys = SystemAccess()
    pro = Program()
    pro.tierOne()
