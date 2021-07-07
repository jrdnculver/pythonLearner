
# import tkinter libary as tk

from tkinter import Label, font
import tkinter as tk
''' Program name: GUI Temperature Converter
    Author: Jordan Culver
    Date: 7/6/2021
    Summary: This program will allow for a user input as an integer or floating number, and in event driven fashion, based on the button
                they choose to press, will convert their input value to fahrenheit or celsius degrees. '''

'''
Buttons, Labels, and Entries are explicit in the program and defined by their method;
TempUnits; class; type class
self.window; the window attribute for class; variable
self.font; sets the font and size of selected widgets; tuple
padding; adds padding; int
width; defines width; int
height; defines height; int
sign; represents degree sign; ?
temp; retrieval value from entry box; str, but cast to float upon calculation
'''

# creating class TempUnits


class TempUnits():
    def __init__(self, window):
        self.window = window
        self.font = ("Courier", "20")

    # will run the program
    def main(self):
        self.windowInfo()
        self.labels()
        self.buttons()
        self.entries()
        self.window.mainloop()

    # configure programming geometry, title, and color
    def windowInfo(self):
        self.window.geometry("400x400")
        self.window.title("School GUI!")
        self.window.config(bg="blue")

    # creating and displaying buttons for user interaction (celsius, fahrenheit, and exit)
    def buttons(self):
        padding = 5
        wid = 10
        hei = 3
        self.celsusButton = tk.Button(
            self.window, text="Celsius", padx=padding, width=wid, height=hei, bg="orange", fg="blue", command=self.convertToCelsius)
        self.fahrButton = tk.Button(
            self.window, text="Fahrenheit", padx=padding, width=wid, height=hei, bg="orange", fg="blue", command=self.convertToFahr)
        self.exitButton = tk.Button(
            self.window, text="Exit", padx=padding, width=wid, height=hei, bg="orange", fg="blue", command=exit)
        self.celsusButton.place(relx=.2, rely=.6, anchor="center")
        self.fahrButton.place(relx=.5, rely=.6, anchor="center")
        self.exitButton.place(relx=.8, rely=.6, anchor="center")

    # creating and displaying label header for program
    def labels(self):
        self.headingLabel = tk.Label(
            self.window, text="Temperature Conversion", font=self.font, bg="orange", fg="blue")
        self.headingLabel.place(relx=.5, rely=.15, anchor="center")

    # method association with celsius button to convert value to celsius
    def convertToCelsius(self):
        sign = u'\N{DEGREE SIGN}'
        temp = self.e1.get()
        self.celsius = 5 / 9 * (float(temp) - 32)
        self.celLabel = tk.Label(
            self.window, text=f"{self.celsius:.2f}" + f"{sign}C", bg="orange", fg="blue", font=self.font, width="20")
        self.celLabel.place(
            relx=.5, rely=.8, anchor="center")

    # method association with fahrenheit button to convert value to fahrenheit
    def convertToFahr(self):
        sign = u'\N{DEGREE SIGN}'
        temp = self.e1.get()
        self.fahr = (float(temp) * 9 / 5) + 32
        self.fahLabel = tk.Label(
            self.window, text=f"{self.fahr:.2f}" + f"{sign}F", bg="orange", fg="blue", font=self.font, width="20")
        self.fahLabel.place(relx=.5, rely=.8, anchor="center")

    # entry box for user input
    def entries(self):
        self.e1 = tk.Entry(self.window, bg="orange", fg="blue",
                           width="30", font=("Courier", "15"))
        self.e1.place(relx=.5, rely=.35, anchor="center", height="30")


if __name__ == "__main__":
    root = tk.Tk()
    gui = TempUnits(root)
    gui.main()
