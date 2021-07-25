from pathlib import Path
from tkinter.filedialog import askopenfilename, asksaveasfile, askdirectory
from tkinter.constants import ANCHOR, DISABLED, S
from tkinter import *
import tkinter as tk
import os
from typing import AnyStr
import pyodbc
import json

# Runs program


class Program:
    newValue = {}

    def __init__(self, name):
        self.name = name

    def formOne(self):
        sql.createLoadTable("loadedFiles")
        sql.readLoadedTable()
        gui.rootProperties()
        gui.rootCanvas()
        gui.rootLabels()
        gui.rootButtons()
        gui.rootText()
        gui.rootOptionMenu()
        gui.root.mainloop()

    def formTwo(self):
        gui.frameProperties()
        gui.frameCanvas()
        gui.frameLabel()
        gui.frameText()
        gui.frameEntries()
        fhand.disperseSaveFile()
        gui.frameOptionMenu()
        gui.frameOptionMenuTwo()
        gui.frameButtons()
        gui.root.mainloop()

# data class for sql storage


class data:
    def __init__(self, numFile, stringFile):
        self.numFile = numFile
        self.stringFile = stringFile

# gui class using tkinter


class Gui:
    def __init__(self, root):
        self.root = root
        newValue = StringVar()

    # main form = root formOne
    # expresses properties of main tkinter form

    def rootProperties(self):
        self.root.geometry("700x500")
        self.root.configure(bg="white")
        self.root.title("File Runner")

    # canvas on main tkinter form

    def rootCanvas(self):
        self.canvasOne = tk.Canvas(self.root, bg="green")
        self.canvasOne.place(relwidth=.82, relheight=.8, relx=.1, rely=.1)

    # label on main tkinter form

    def rootLabels(self):
        self.mainStatusLabel = tk.Label(
            self.root, bg="green", fg="white", text=sql.mainStatus)
        self.mainStatusLabel.place(relx=.5, rely=.14, anchor="center")

    # text widget placed on main form

    def rootText(self):
        self.textRoot = tk.Text(
            self.canvasOne, bg="white", font=("cambria", 8), )
        self.textRoot.place(relwidth=.8, relheight=.6,
                            relx=.1, rely=.1)
        self.textRoot.insert(tk.END, "Added Files \n", "textOneHeader")
        self.textRoot.tag_configure(
            "textOneHeader", justify="center", font=("poor Richard", 14))

    # buttons placed on main form

    def rootButtons(self):
        self.openFileBtn = tk.Button(self.root, text="Open", bg="white", command=lambda: [
                                     fhand.fileSelector()])
        self.openFileBtn.place(rely=.83, relx=.21, width=90,
                               height=30, anchor="center")

        self.loadFileBtn = tk.Button(self.root, text="To Screen", bg="white", command=lambda: [
                                     fhand.disperseFiles()])
        self.loadFileBtn.place(rely=.83, relx=.41, width=90,
                               height=30, anchor="center")

        self.runFileBtn = tk.Button(self.root, text="Run", bg="white", command=lambda: [fhand.runFile()
                                                                                        ])
        self.runFileBtn.place(rely=.83, relx=.61, width=90,
                              height=30, anchor="center")

        self.deleteFileBtn = tk.Button(self.root, text="Delete All", bg="white", command=lambda: [fhand.deleteFiles()
                                                                                                  ])
        self.deleteFileBtn.place(rely=.83, relx=.81, width=90,
                                 height=30, anchor="center")

        self.saveFileBtn = tk.Button(self.root, text="Modify", bg="green", fg="white", command=lambda: [pro.formTwo()
                                                                                                        ])
        self.saveFileBtn.place(rely=.05, relx=.17, width=90,
                               height=30, anchor="center")

    # option menu for selection of saved configurations

    def rootOptionMenu(self):
        self.variable = StringVar(self.root)
        self.variable.set(sql.savedTables[0])
        self.optionMenuOne = tk.OptionMenu(
            self.root, self.variable, *sql.savedTables)
        self.optionMenuOne.place(
            width=150, height=35, relx=.705, rely=.02)
        self.optionMenuOne.config(
            background="green", foreground="white", )
        self.optionMenuOne["menu"].config(bg="grey")

    # duplicate option menu for formTwo

    def frameOptionMenu(self):
        self.variable = StringVar(self.root)
        self.variable.set(sql.savedTables[0])
        self.optionMenuOne = tk.OptionMenu(
            self.frameOne, self.variable, *sql.savedTables)
        self.optionMenuOne.place(
            width=150, height=35, relx=.705, rely=.02)
        self.optionMenuOne.config(
            background="green", foreground="white", )
        self.optionMenuOne["menu"].config(bg="grey")

    def frameOptionMenuTwo(self):
        options = ["Choose Save", "Files", "Database"]
        self.variableTwo = StringVar(self.root)
        self.variableTwo.set(options[0])
        self.optionMenuOne = tk.OptionMenu(
            self.frameOne, self.variableTwo, *options)
        self.optionMenuOne.place(
            width=150, height=35, relx=.1, rely=.02)
        self.optionMenuOne.config(
            background="green", foreground="white", )
        self.optionMenuOne["menu"].config(bg="grey")

    # frameOne = formTwo
    # form is for saving configuration
    # properties for associated form2

    def frameProperties(self):
        self.frameOne = tk.Frame(self.root, bg="white")
        self.frameOne.place(relwidth=1, relheight=1)

    # frame labels for frameOne

    def frameLabel(self):
        self.frameLabelOne = tk.Label(self.frameOne, text="Save Configuration", background="green", foreground="white", font=(
            "poor Richard", 14))
        self.frameLabelOne.place(relx=.5, rely=.2, anchor="center")

        self.frameLabelTwo = tk.Label(
            self.frameOne, text="Saved Name: ", background="green", foreground="white", font=("poor Richard", 11))
        self.frameLabelTwo.place(rely=.27, relx=.12)

        self.frameLabelThree = tk.Label(
            self.frameOne, text=sql.saveStatus, background="green", foreground="white", font=("poor Richard", 11))
        self.frameLabelThree.place(rely=.38, relx=.5, anchor="center")

    # textbox for frameOne

    def frameText(self):
        self.textFrame = tk.Text(
            self.frameOne, bg="white", foreground="green", font=("poor Richard", 8))
        self.textFrame.place(height=220, width=500,
                             rely=.63, relx=.5, anchor="center")

    # canvas placed on frameOne for contrast

    def frameCanvas(self):
        self.frameCanvasOne = tk.Canvas(self.frameOne, background="green")
        self.frameCanvasOne.place(relwidth=.82, relheight=.8, rely=.1, relx=.1)

    # frame entries placed to get name of new saved configuration

    def frameEntries(self):
        self.frameEntryOne = tk.Entry(self.frameOne)
        self.frameEntryOne.place(
            height=28, width=125, relx=.33, rely=.29, anchor="center")

    def frameButtons(self):
        self.sqlSaveFileBtn = tk.Button(self.frameOne, text="Save", bg="green", fg="white", command=lambda: [sql.saveConfigurations()
                                                                                                             ])
        self.sqlSaveFileBtn.place(rely=.29, relx=.50, width=90,
                                  height=30, anchor="center")

        self.sqlDeleteFileBtn = tk.Button(self.frameOne, text="Delete", bg="green", fg="white", command=lambda: [sql.delete()
                                                                                                                 ])
        self.sqlDeleteFileBtn.place(rely=.29, relx=.65, width=90,
                                    height=30, anchor="center")

        self.menuBtn = tk.Button(self.frameOne, text="Back", bg="green", fg="white", command=lambda: [gui.frameOne.destroy(), pro.formOne()
                                                                                                      ])
        self.menuBtn.place(rely=.29, relx=.80, width=90,
                           height=30, anchor="center")

# class to receive and run files


class FileHandler:
    def __init__(self):

        # files added are appended to this list

        self.fileHolder = []

        # files are added to this dictionary prior to sql injection

        self.savedDict = {}

    # selects file and brings in string form to program

    def fileSelector(self):
        file = askopenfilename(filetypes=(
            ("Executables", "*.exe"), ("All files", "*.*")), title='Open File', initialdir=str(Path.home()))
        if file not in self.fileHolder and file != "":
            self.fileHolder.append(file)

    # takes files that have been selected and places the string value in the textRoot box

    def disperseFiles(self):
        if sql.getOptionMenuValue() != "Load Configuration":
            sql.getOptionMenuValue()
            # will try to load from database
            try:
                sql.getloadedTableConfigs()
                gui.textRoot.delete(1.0, tk.END)
                gui.textRoot.insert(tk.END, "Added Files \n", "textOneHeader")
                for x in self.fileHolder:
                    gui.textRoot.insert(tk.END, x + "\n", "fileNames")
                    gui.textRoot.tag_configure(
                        "fileNames", justify="center", font=("poor Richard", 11))
            except:
                # will try to load from file
                try:
                    fhand.fromFileReader()
                except:
                    # will keep program from crashing and user indication
                    sql.mainConfigStatusLabel(
                        "That File or Database does not Exist")
        else:
            # if user is adding files manually
            try:
                i = 0
                gui.textRoot.delete(1.0, tk.END)
                gui.textRoot.insert(tk.END, "Added Files \n", "textOneHeader")
                for x in self.fileHolder:
                    gui.textRoot.insert(tk.END, x + "\n", "fileNames")
                    gui.textRoot.tag_configure(
                        "fileNames", justify="center", font=("poor Richard", 11))
                    self.savedDict[i] = x
                    i += 1
            except:
                sql.mainConfigStatusLabel(
                    "That File or Database does not Exist")

            # takes file and show in save page text box

    def disperseSaveFile(self):
        for x in self.fileHolder:
            gui.textFrame.insert(tk.END, x + "\n")

    # will run the files that exist in the fileHolder list

    def runFile(self):
        for x in self.fileHolder:
            os.startfile(x)

    # will delete files from list to ensure duplicates dont occur in the textRoot box
    # allows user to start fresh

    def deleteFiles(self):

        self.fileHolder.clear()
        gui.textRoot.delete(1.0, tk.END)
        gui.textRoot.insert(tk.END, "Added Files \n", "textOneHeader")

    # creates dictionary for storage in sql

    def createDict(self):
        i = 0
        for x in fhand.fileHolder:
            fhand.savedDict[i] = x
            i += 1

    # will read file to program

    def fromFileReader(self):
        fhand.fileHolder.clear()
        with open(f"configurations.json", "r") as fp:
            readFile = json.load(fp)
        fhand.deleteFiles()
        for files in readFile:
            for key, value in files[0].items():
                for val in value:
                    if key == sql.getOptionMenuValue():
                        fhand.fileHolder.append(val)
                    if files[1] not in sql.savedTables:
                        sql.savedTables.append(files[1])
        gui.textRoot.delete(1.0, tk.END)
        gui.textRoot.insert(tk.END, "Added Files \n", "textOneHeader")
        for x in self.fileHolder:
            gui.textRoot.insert(tk.END, x + "\n", "fileNames")
            gui.textRoot.tag_configure(
                "fileNames", justify="center", font=("poor Richard", 11))

    # will write file for program

    def toFileWriter(self):
        tempList = []
        if os.path.exists("configurations.json"):
            with open("configurations.json", "r") as fp:
                readFile = json.load(fp)
                for line in readFile:
                    tempList.append(line)
        fhand.savedDict.clear()
        writer = sql.getTableName()
        fhand.savedDict[f"{writer}"] = fhand.fileHolder
        if fhand.savedDict not in tempList:

            tempList.append([fhand.savedDict, writer])
        with open(f"configurations.json", "w") as fp:
            json.dump(tempList, fp)
        if writer not in sql.savedTables:
            sql.savedTables.append(writer)
        fp.close()
        sql.configStatusLabel(f"Configuration saved as {writer}")

    # gets user feedback for where to save data

    def getSaveDestination(self):
        self.fileDestination = gui.variableTwo.get()
        return self.fileDestination


# class to allow long term storage of selection configurations


class SQL:
    def __init__(self):
        self.conn = conn = pyodbc.connect(
            "Driver={SQL SERVER Native Client 11.0};"
            "Server=JORDANPC\SQLEXPRESS;"
            "Database=person;"
            "Trusted_Connection=yes;"
        )
        self.cursor = conn.cursor()
        self.savedTables = ["Load Configuration"]
        self.tableName = ""
        self.saveStatus = "CONFIGURATION UNSAVED"
        self.mainStatus = ""

    # read load table and give value to saved table list to show in option menu widget

    def readLoadedTable(self):
        self.loadedResults = self.cursor.execute("select * from loadedFiles")
        for loadFile in self.loadedResults:
            if loadFile[0] not in self.savedTables:
                self.savedTables.append(loadFile[0])

        if os.path.exists("configurations.json"):
            with open(f"configurations.json", "r") as fp:
                readFile = json.load(fp)
                for files in readFile:
                    if files[1] not in self.savedTables:
                        self.savedTables.append(files[1])

    # will retrieve saved loaded table values based on option menu choice

    def getloadedTableConfigs(self):
        self.loadedResults = self.cursor.execute(
            f"select * from {self.optionMenuValue}")
        for loadFile in self.loadedResults:
            if loadFile[1] not in fhand.fileHolder:
                fhand.fileHolder.append(loadFile[1])

    # gets value from option menu to return saved configs from sql

    def getOptionMenuValue(self):
        self.optionMenuValue = gui.variable.get()
        return self.optionMenuValue

    # gets input from user on what the name of store configuratino will be

    def getTableName(self):
        self.tableName = gui.frameEntryOne.get()
        return self.tableName

    # will dictate status label output

    def configStatusLabel(self, status):
        self.saveStatus = status
        gui.frameOne.destroy()
        pro.formTwo()

    # will dictate status label output for main page
    def mainConfigStatusLabel(self, status):
        self.mainStatus = status
        pro.formOne()

    # will create a user defined new table to store user configuration

    def createNewTable(self):
        self.cursor.execute(
            f"create table {self.tableName} (numFile integer, stringFile nvarchar(100));")

    # creates load table, if not created, for storage and communication of saved confiurations

    def createLoadTable(self, loadTable):
        self.cursor.execute(
            f"if object_ID('{loadTable}', 'U') is NULL create table {loadTable} (loadFile nvarchar(100));")

        self.conn.commit()

    # will delete loadedTable if need (currently unused)

    def deleteLoadedTable(self, loadTable):
        self.cursor.execute(
            f"if object_ID('{loadTable}', 'U') is NOT NULL drop table {loadTable};")

    # will update table with saved configuration

    def updateConfigTable(self):
        self.tableName = self.getTableName()
        if self.tableName != "":
            for id, name in fhand.savedDict.items():
                data.numFile = int(id)
                data.stringFile = name

                self.cursor.execute(f'insert into {self.tableName} (numFile, stringFile) values (?,?);',
                                    (data.numFile, data.stringFile))
        self.conn.commit()

    # update sql with saved loadedFiles

    def updateSavedTable(self):
        if self.savedTables != 0:
            for x in self.savedTables:
                x = x
            self.cursor.execute(
                f"insert into loadedFiles (loadFile) values (?);", (x))

        self.conn.commit()

    # will delete a stored table

    def delete(self):
        self.tableName = self.getTableName()
        try:
            if self.tableName != "":
                self.savedTables.remove(self.tableName)
                if os.path.exists("configurations.json"):
                    with open(f"configurations.json", "r") as fp:
                        readFile = json.load(fp)
                        print("loaded")
                    i = 0
                    for files in readFile:
                        if files[1] == self.tableName:
                            print(files[1], self.tableName)
                            readFile.remove(readFile[i])
                            print("files removed")
                    with open(f"configurations.json", "w") as fp:
                        json.dump(readFile, fp)
                        with open(f"configurations.json", "r") as fp:
                            readFile = json.load(fp)
                            i = 0
                            for files in readFile:
                                if self.tableName == files[1]:
                                    sql.savedTables.remove(readFile[i])
                                i += 1

                    print("files written")
        except:
            try:
                if self.tableName != "":
                    self.cursor.execute(f"drop table {self.tableName}")
                    self.cursor.execute(
                        f"delete from LoadedFiles where loadFile = '{self.tableName}'")
                    if self.tableName in self.savedTables:
                        self.savedTables.remove(self.tableName)

                    self.conn.commit()
                    self.configStatusLabel("CONFIGURATION DELETED")
            except:
                self.configStatusLabel("CONFIGURATION DELETED")

    # will save the configuration to an sql table named by user

    def saveConfigurations(self):
        if fhand.getSaveDestination() == "Choose Save":
            self.configStatusLabel("You must choose a save destination")
        elif fhand.getSaveDestination() == "Database":
            self.tableName = self.getTableName()
            fhand.savedDict.clear()
            if self.tableName != "":
                self.createNewTable()
                fhand.createDict()
                self.updateConfigTable()
                self.savedTables.append(self.tableName)
                self.updateSavedTable()
                self.configStatusLabel("CONFIGURATION SAVED")
        elif fhand.getSaveDestination() == "Files":
            fhand.toFileWriter()


if __name__ == "__main__":
    root = tk.Tk()
    gui = Gui(root)
    fhand = FileHandler()
    sql = SQL()
    pro = Program("File Runner")
    pro.formOne()
