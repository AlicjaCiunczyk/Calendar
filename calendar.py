"""This is a personal calendar. It lets user add, remove, edit and view events
in the calendar"""
from time import sleep, strftime

OWNER_NAME = input('Add your name: ')
calendar = {}


def welcome():
    print("Welcome " + OWNER_NAME + ".")
    print("The calendar is opening...")
    sleep(1)
    print("Today is: " + strftime("%A %B %d, %Y"))
    print("The time is: " + strftime("%H : %M : %S"))
    sleep(1)
    print("What would you like to do?")


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