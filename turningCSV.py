import csv
import os
import tkinter as tk
from tkinter.constants import END
import pandas as pd


class Program:
    def __init__(self):
        self.Information = []

    # Run program Gui
    def main(self):
        gui.rootProperties()
        gui.textProperties()
        gui.labelProperties()
        gui.textButton()
        gui.listBoxProperties()
        gui.root.mainloop()


class CreateCSV:
    def __init__(self, fileName):
        # Sets file name
        self.fileName = fileName
        # Empty list for fields
        self.fields = []
        # Empty column for string version of column
        self.columns = ""
        # Empty list for records
        self.records = []
        # Hold Read Records
        self.recordHold = []

    def setFields(self):
        # Getting value from columnEntry and modifying
        fields = gui.columnEntry.get("1.0", 'end-1c')
        # Ensures stringify of fields and splits with ","; becomes a list
        fields = str(fields).split(",")
        # Iterates through and stips white space form each value in list
        for field in fields:
            field = field.strip()
            field = ",".join(field)
            # Appends each new value to self.fields
            if fields not in self.fields:
                # Appending column Names for Excel Sheet
                self.fields.append(fields)
        print("Fields", self.fields)

    def setRecords(self):
        # Getting value from rowEntry and modifying
        record = gui.multiRowEntry.get("1.0", 'end-1c')
        # Ensures stringify of fields and splits with "\n"; becomes a list
        records = str(record).split("\n")
        # Iterates through records and stips whitespace and appends to self.records
        for record in records:
            # Creating a list of records
            recordList = record.split(",")
            # Ensuring there are no duplicates
            if recordList not in self.records:
                # Appending records to final record list
                self.records.append(recordList)

        print("Records", self.records)

    def setInformation(self):
        pro.Information.clear()
        # Concatenating self.fields and self.records to make up final list of values called pro.Information
        # Defined in the program class
        pro.Information = self.fields + self.records
        # Checking to see if the fileName exist
        if os.path.exists(self.fileName):
            # If file exist, will read and get values from past inputs
            self.readCSV()

        print("Information", pro.Information)

    def writeCSV(self):
        # creating fileName for CSV file
        with open(self.fileName, 'w') as file:
            # Setting fileName as file and declaring delimiter as ","
            writer = csv.writer(file, delimiter=',')
            # Iterating through each record entered and writing it to the CSV file
            for info in pro.Information:
                # Remove all spaces
                if info != "":
                    # Write info to the CSV file
                    writer.writerow(info)

    def readCSV(self):
        # Clear recordHold to prevent duplicates with multiple inputs
        self.recordHold.clear()
        # Read csv file
        with open(self.fileName, 'r',) as file:
            # Defining reader object to read CSV file
            reader = csv.reader(file, delimiter=',')
            # Iterating rows of reader
            for row in reader:
                # Appending each row to list self.recordHold
                self.recordHold.append(row)
            # Iterating list to remove any values that are empty
            for empty in self.recordHold:
                # Removing values that are null
                if empty == []:
                    self.recordHold.remove(empty)
            # Removing the header columns to prevent duplicates from occuring in our final list
            self.recordHold.remove(self.recordHold[0])
            # Appending the rest of our values from the reading to pro.Information for display
            for records in self.recordHold:
                if records not in pro.Information:
                    pro.Information.append(records)
        # returning our updates version of pro.Information
        # return pro.Information
        print("RecordHold", self.recordHold)

    def createExcel(self):
        # Want to create same name from CSV file to Excel File
        # Pandas reading csv file
        excelFile = pd.read_csv(
            self.fileName)
        # Setting changeFileName = self.fileName
        changeFileName = self.fileName
        # Splitting string at "."
        changeFileName = changeFileName.split(".")
        # Referencing first portion of string
        fileStart = changeFileName[0]
        # Defining second portion of string as excel file
        fileExtension = "xlsx"
        # Clearing list if an values exist
        changeFileName.clear()
        # Appending first value to list
        changeFileName.append(fileStart)
        # Appending seconf value to list
        changeFileName.append(fileExtension)
        # Joining values to makes excel file name
        excelfileName = ".".join(changeFileName)
        # Creating Excel File
        excelFile.to_excel(
            excelfileName, index=None, header=True)


class Gui():
    def __init__(self, root):
        self.root = root
    # Creating root properties of window

    def rootProperties(self):
        self.root.geometry("1000x500")
        self.root.configure(bg="black")
        self.root.title("Med Chron Input")
    # Creating label properties

    def labelProperties(self):
        self.labelHead = tk.Label(
            self.root, text="Data Input", background="black", foreground="white", font=("Rockwell", 20),)
        self.labelHead.place(relx=.25, rely=.08, anchor="center")

        self.columnLabel = tk.Label(self.root, text="Enter Columns separated by commas",
                                    background="black", foreground="white", font=("Rockwell", 10),)
        self.columnLabel.place(relx=.03, rely=.15)

        self.recordLabel = tk.Label(self.root, text="Enter record values separated by commas (No comma after final value of single record)",
                                    background="black", foreground="white", font=("Rockwell", 10),)
        self.recordLabel.place(relx=.03, rely=.3)
    # Creating text Properties

    def textProperties(self):
        self.columnEntry = tk.Text(self.root)
        self.columnEntry.place(relwidth=.39, relheight=.1, relx=.03, rely=.2)
        self.multiRowEntry = tk.Text(self.root)
        self.multiRowEntry.place(relwidth=.5, relheight=.5, relx=.03, rely=.35)
    # Creating Button properties

    def textButton(self):
        self.columnButton = tk.Button(
            self.root, text="Submit", bg="white", fg="black", font=("Rockwell", 12), command=lambda: [cCSV.setFields(), cCSV.setRecords(), cCSV.setInformation(), gui.populateListbox()])
        self.columnButton.place(relwidth=.1, relheight=.1, relx=.43, rely=.2)

        self.writeButton = tk.Button(
            self.root, text="To CSV", bg="white", fg="black", font=("Rockwell", 12), command=lambda: [cCSV.writeCSV()])
        self.writeButton.place(relwidth=.3, relheight=.05,
                               relx=.3, rely=.92, anchor="center")

        self.excelButton = tk.Button(
            self.root, text="To Excel", bg="white", fg="black", font=("Rockwell", 12), command=lambda: [cCSV.createExcel()])
        self.excelButton.place(relwidth=.3, relheight=.05,
                               relx=.7, rely=.92, anchor="center")

    # Creating List Box
    def listBoxProperties(self):
        self.primaryListBox = tk.Listbox(self.root)
        self.primaryListBox.place(
            relwidth=.43, relheight=.80, relx=.55, rely=.05)

    # Function to populate values from information list upon submitting values
    def populateListbox(self):
        self.primaryListBox.delete(0, END)
        self.primaryListBox.insert("end", *pro.Information)


if __name__ == "__main__":
    cCSV = CreateCSV("law.csv")
    root = tk.Tk()
    gui = Gui(root)
    pro = Program()
    pro.main()
