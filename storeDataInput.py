''' Program name: Store Totals for Sales
    Author: Jordan Culver
    Date: 6/26/2021
    Summary: This program is meant to end with taking the total sales and expressing that value to the user.'''

''' 
store.name; the name of the store; string
record.addRecord; flag; string/char
record.storeTotal; list for holding daily inputs; float/string (for file input)
record.totalSales; user input for sales; float
cal.validDate; formatted date; string
cal.checkingInfo; flag; string/char
record.total; sum of storeTotal list; float
record.average; average of storeTotal list; float
cal.dayOfWeek; dictionary of days of week; int/string
cal.month; dictionary of months of year; int/string
cal.year; the year; string
cal.monthChoice; value for month choice; int
cal.chosenMonth; month chosen; string
cal.day; day of the month; int
cal.daysOfWeekChoice; value for day of week chosen; int
cal.daysOfWeekChosen; day chosen; string
cal.saveDate; list of saved dates; string
cal.firstDate; first date in saveDate list; string
cal.lastDate; last date in saveDate list; string

'''

# Wanted to attempt OOP for this program
# Program utilizes list and shows how loop can calculate total for the submissions
# Allows user to select date and can enter as many days at a time as he/she wants

# Store Object


class Store():
    def __init__(self, name):
        self.name = name

    def main(self):
        store.greeting()
        while record.addRecord == "Y":
            record.inputtingData()
            record.displayingData()
            record.addingAnotherRecord()
        record.totals()
    # Greet the user

    def greeting(self):
        print(f"\nWelcome to Inputting Data Program.")
        print(f"\nThe current store is: {self.name}")
        print("=" * 50)
        print("Preparing Data Input")
        print("=" * 50)

# Record Book object for data collection


class RecordBook():
    def __init__(self):
        self.addRecord = "Y"
        self.storeTotal = []

    def inputtingData(self):
        # Calls on calendar object class to get date value for record keeping
        cal.main()
        # Getting daily sales input
        self.totalSales = float(
            input("\nWhat were the sales for this day? (Ex 511.23): "))
        self.totalSales = f"{self.totalSales:.2f}"
        self.totalSales = float(self.totalSales)
        self.storeTotal.append(self.totalSales)

    def displayingData(self):
        print(self.totalSales)
    # Ask user if they want another daily input

    def addingAnotherRecord(self):
        self.addRecord = input(
            "\nDo you have another day of Sales you would like to input? (Y or N): ").capitalize()
        if self.addRecord == "Y":
            cal.checkingInfo = " "

    # Math for sum of inputs and averages

    def totals(self):
        # Using a loop to get total, but can also use list function
        # self.total = 0
        # for value in self.storeTotal:
        #     self.total += value
        self.total = sum(self.storeTotal)
        self.average = self.total / len(self.storeTotal)
        self.total = f"{self.total:.2f}"
        self.average = f"{self.average:.2f}"
        print("=" * 50)
        print(
            f'The dates included range:\nFROM: {cal.firstDate}\nTO: {cal.lastDate}')
        print(f'\nThe Input Total for this data was: ${self.total}')
        print(
            f'\nThe average for this data over {len(self.storeTotal)} day(s) was: ${self.average}')
        print("=" * 50)

# Calendar object to get current input date


class Calendar():
    def __init__(self):
        self.dayOfWeek = {1: "Monday", 2: "Tuesday", 3: "Wednesday",
                          4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
        self.month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                      9: "September", 10: "October", 11: "November", 12: "December"}
        self.checkingInfo = " "
        self.dateSave = []
        self.validDate = " "

    def main(self):
        while self.checkingInfo != "Y":
            self.chooseYear()
            self.chooseMonth()
            self.chooseDay()
            self.chooseDayOfWeek()
            self.date()
            self.datecheck()
    # define Year

    def chooseYear(self):
        while True:
            try:
                self.year = input(
                    "\nWhat is the Year for your Sales input? (Ex 2021): ")
                if len(self.year) == 4:
                    break
                else:
                    raise Exception
            except:
                print("\nThat is not a valid year.  Please enter another year.")
    # define month

    def chooseMonth(self):
        if self.validDate != " ":
            print("=" * 50)
            print(f"The previous date input was: {self.validDate}")
            print("=" * 50)
        print("\nMonths of the Year: ")
        print("=" * 50)
        for key, value in self.month.items():
            print(f"{key:2}:", f"{value[0:3]}")
        self.monthChoice = int(
            input("\nWhat Month would you like to choose for Sales input?: "))
        self.chosenMonth = self.month.get(self.monthChoice)
    # define day

    def chooseDay(self):
        if self.validDate != " ":
            print("=" * 50)
            print(f"The previous date input was: {self.validDate}")
            print("=" * 50)
        while True:
            try:
                self.day = int(
                    input("\nPlease Enter the day for your Sales input (Ex 15): "))
                if self.monthChoice == 1 or self.monthChoice == 3 or self.monthChoice == 5 or self.monthChoice == 7 or self.monthChoice == 8 or self.monthChoice == 10 or self.monthChoice == 12:
                    if self.day > 0 and self.day < 32:
                        break
                    else:
                        raise Exception
                elif self.monthChoice == 4 or self.monthChoice == 6 or self.monthChoice == 9 or self.monthChoice == 11:
                    if self.day > 0 and self.day < 31:
                        break
                    else:
                        raise Exception
                else:
                    if self.monthChoice == 2:
                        if self.day > 0 and self.day < 30:
                            break
                        else:
                            raise Exception
            except:
                print("\nThat is not a valid day for this month.  Enter another day.")
    # choose day of week

    def chooseDayOfWeek(self):
        if self.validDate != " ":
            print("=" * 50)
            print(f"The previous date input was: {self.validDate}")
            print("=" * 50)
        print("\nDays of the Week: ")
        print("=" * 50)
        for key, value in self.dayOfWeek.items():
            print(f"{key}: {value}")
        self.daysOfWeekChoice = int(
            input("\nWhat day of week would you like to choose for your Sales input?: "))
        self.chosenDayOfWeek = self.dayOfWeek.get(self.daysOfWeekChoice)
    # formatted version of date

    def date(self):
        self.validDate = (
            f"\n{self.chosenDayOfWeek}, {self.chosenMonth} {self.day}, {self.year}".strip("\n"))
        self.dateSave.append(self.validDate)
        self.firstDate = self.dateSave[0]
        self.lastDate = self.dateSave[-1]

        print("=" * 50 + f"\n{self.validDate}")
        print("=" * 50)
    # flag to ensure correct date outcome

    def datecheck(self):
        self.checkingInfo = input(
            "\nIs this the correct date for Sales input? (Y or N): ").capitalize()


if __name__ == "__main__":
    cal = Calendar()
    store = Store("Big Business")
    record = RecordBook()
    store.main()
