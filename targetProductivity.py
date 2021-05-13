import tkinter as tk

root = tk.Tk()
root.title("Hours to Work")
root.geometry("300x300")
root.config(bg="black")


entryTreatMin = tk.Entry(root, width=20, borderwidth=5)
entryTreatMin.place(relx=.5, rely=.19)

entryProdTarg = tk.Entry(root, width=20, borderwidth=5)
entryProdTarg.place(relx=.5, rely=.30)

entryClockInTime = tk.Entry(root, width=20, borderwidth=5)
entryClockInTime.place(relx=.5, rely=.41)

entryLunchBreakMin = tk.Entry(root, width=20, borderwidth=5)
entryLunchBreakMin.place(relx=.5, rely=.52)

#################################################################################


def mainEnter():
    treatmin = entryTreatMin.get()
    prodTarg = entryProdTarg.get()
    clockInTime = entryClockInTime.get()
    lunchTime = entryLunchBreakMin.get()

    targetWorkMin, answer, accuracy = determineWorkMin(treatmin, prodTarg)
    hourTarget, minuteTarget, hours, minutes = prepTime(
        clockInTime, targetWorkMin, accuracy)
    durationTargetHour, durationTargetMin, totalDuration = gettingTargetProduction(
        hourTarget, minuteTarget)
    targetClockOut = makingClock(
        durationTargetHour, durationTargetMin, hours, minutes, lunchTime, accuracy)
    presentingLabels(answer, totalDuration, targetClockOut)


def determineWorkMin(treatmin, prodTarg):
    # Simple math to get and print target work minutes
    targetWorkMin = float(treatmin) / float(prodTarg)
    answer = float("{:.0f}".format(targetWorkMin))
    answer = f"{answer} Min"
    accuracy = str(int(targetWorkMin))
    accuracy = accuracy[-1]

    return targetWorkMin, answer, accuracy


def prepTime(clockInTime, targetWorkMin, accuracy):
    # Splitting to separate hours and minutes
    values = clockInTime.split(":")
    hours = values[0]
    minutes = values[1]

    # Inputs are strings, casting to integer
    hours = int(hours)
    minutes = int(minutes)
    targetWorkMin = int(targetWorkMin)

    # # Converting all values to minutes
    # getMinutes = (hours * 60) + minutes
    # totalTime = getMinutes + targetWorkMin

    # Converting presentation for target work label
    hourTarget = targetWorkMin / 60
    minuteTarget = targetWorkMin % 60

    if int(accuracy) >= 5:
        minuteTarget += 1

    return hourTarget, minuteTarget, hours, minutes


def gettingTargetProduction(hourTarget, minuteTarget):
    # Cleaning data by removing decimal values from quotient and remainder
    singleTargetHour = str(hourTarget).split(".")
    durationTargetHour = singleTargetHour[0]
    singleTargetMin = str(minuteTarget).split(".")
    durationTargetMin = singleTargetMin[0]

    totalDuration = (f"{durationTargetHour} Hrs {durationTargetMin} Min")

    return durationTargetHour, durationTargetMin, totalDuration


def makingClock(durationTargetHour, durationTargetMin, hours, minutes, lunchTime, accuracy):

    newHour = int(durationTargetHour)
    newMinute = int(durationTargetMin)

    finalHour = hours + newHour
    if lunchTime == "":
        finalMinute = minutes + newMinute
    else:
        finalMinute = minutes + newMinute + int(lunchTime)

    # Casting to ensure values are integers for calculations
    finalHour = int(finalHour)
    finalMinute = int(finalMinute)

    if finalMinute > 60:
        finalMinute = finalMinute - 60
        finalHour += 1
    else:
        pass

    suffix = "AM"
    if finalHour >= 12:
        finalHour = finalHour - 12
        suffix = "PM"
        if finalHour >= 12:
            finalHour = finalHour - 12
            suffix = "AM"
    if finalHour == 0:
        finalHour = 12

    # Tidy presentation with appropriate 0 prior to the 10 minute value
    if finalMinute in range(0, 10):
        finalMinute = str(finalMinute)
        finalMinute = "0" + finalMinute

    targetClockout = f"{str(finalHour)}:{finalMinute} {suffix}"

    return targetClockout


def presentingLabels(answer, totalDuration, targetClockout):

    labelTargetWorkMin = tk.Label(
        root, width=17, borderwidth=5, bg="green", fg="white", text=answer)
    labelTargetWorkMin.place(relx=.5, rely=.63)

    labelTargetWorkDur = tk.Label(
        root, width=17, borderwidth=5, bg="green", fg="white", text=totalDuration)
    labelTargetWorkDur.place(relx=.5, rely=.74)

    labelTargetClockOut = tk.Label(
        root, width=17, borderwidth=5, bg="green", fg="white", text=targetClockout)
    labelTargetClockOut.place(relx=.5, rely=.85)


def clearButton():
    entryTreatMin.delete(0, 10)
    entryProdTarg.delete(0, 10)
    entryClockInTime.delete(0, 10)
    entryLunchBreakMin.delete(0, 10)


def buttonsWidgets():
    buttonClear = tk.Button(root, text="Clear", bg="grey",
                            fg="black", width=5, command=clearButton)
    buttonClear.place(relx=.15, rely=.1, anchor="center")

    buttonEnter = tk.Button(root, text="Enter", bg="grey",
                            fg="black", width=5, command=mainEnter)
    buttonEnter.place(relx=.85, rely=.1, anchor="center")


def labelWidgets():
    label = tk.Label(root, text="PRODUCTIVITY PREDICTOR",
                     bg="black", fg="white")
    label.place(relx=.5, rely=.1, anchor="center")

    labelTreatMin = tk.Label(
        root, text="Treatment Minutes", bg="black", fg="white")
    labelTreatMin.place(relx=.25, rely=.23, anchor="center")

    labelProdTarg = tk.Label(
        root, text="Productivity Target", bg="black", fg="white")
    labelProdTarg.place(relx=.25, rely=.34, anchor="center")

    labelClockInTime = tk.Label(
        root, text="Clock in Time (HH:MM)", bg="black", fg="white")
    labelClockInTime.place(relx=.25, rely=.45, anchor="center")

    labelLunchBreak = tk.Label(
        root, text="Lunch Break Minutes", bg="black", fg="white")
    labelLunchBreak.place(relx=.25, rely=.56, anchor="center")

    labelTargWorkMin = tk.Label(
        root, text="Target Working Minutes", bg="black", fg="white")
    labelTargWorkMin.place(relx=.25, rely=.67, anchor="center")

    labelTargetWorkDur = tk.Label(
        root, text="Target Working Duration", bg="black", fg="white")
    labelTargetWorkDur.place(relx=.25, rely=.78, anchor="center")

    labelClockOutTime = tk.Label(
        root, text="Target Clock Out", bg="black", fg="white")
    labelClockOutTime.place(relx=.25, rely=.89, anchor="center")


buttonsWidgets()
labelWidgets()

root.mainloop()
