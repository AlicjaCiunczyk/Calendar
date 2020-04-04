"""This is a personal calendar. It lets user add, remove, edit and view events
in the calendar"""
from time import sleep, strftime
from tkinter import *

OWNER_NAME = input('Add your name: ')
calendar = {}


def welcome():

    root = Tk()
    welcome_ownr = Label(root, text = ("Welcome " + OWNER_NAME + "."))
    welcome_ownr.grid(row = 0, column = 0)
    open_cal = Label(root, text = "The calendar is opening...")
    open_cal.grid(row = 1, column = 0)
    sleep(1)
    date = Label(root, text = "Today is: " + strftime("%A %B %d, %Y"))
    date.grid(row = 2, column = 0)
    time = Label(root, text = "The time is: " + strftime("%H : %M : %S"))
    time.grid(row = 2, column = 1)    
    sleep(1)
    to_do = Label(root, text = "What would you like to do?")
    to_do.grid(row = 3, column = 0)
    root.mainloop()


def start_calendar():

    welcome()
    start = True
    while start:
        user_choice = input("Type A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == "V":
            if len(calendar.keys()) < 1:
                print("Your calendar is empty.")
            else:
                print(calendar)
        elif user_choice == "U":
            if len(calendar.keys()) < 1:
                print("Your calendar is empty.")
                try_again = input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                date = input("What date? ")
                update = input("Enter update: ")
                calendar[date] = update
                print("Update was successful.")
                print(calendar)
        elif user_choice == "A":
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYYY): ")
            if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                print("The date provided is invalid. The event cannot take place in the past.")
                try_again = input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                while try_again not in ["Y", "N"]:
                    try_again = input("Try Again? Y for Yes, N for No: ").upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print("Event added.")
                print(calendar)
        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                print("Calendar is empty.")
            else:
                event = input("What event? ")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del(calendar[date])
                        print("The event was deleted.")
                        print(calendar)
                        break
                    else:
                        print("Cannot delete the event - event does not exist.")
        elif user_choice == "X":
            start = False
            print("The program is exiting. Goodbye.")
        else:
            print("Invalid command. Exiting the program.")
            start = False


start_calendar()







