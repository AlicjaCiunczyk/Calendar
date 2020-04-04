"""This is a personal calendar. It lets user add, remove, edit and view events
in the calendar"""
from time import sleep, strftime

OWNER_NAME = input('Add your name: ')
calendar = {}


def welcome():
    'Specify a user and print a welcome message.'

    print("Welcome " + OWNER_NAME + ".")
    print("The calendar is opening...")
    sleep(1)
    print("Today is: " + strftime("%A %B %d, %Y"))
    print("The time is: " + strftime("%H : %M : %S"))
    sleep(1)
    print("What would you like to do?")


def start_calendar():
    'Create a simple calendar with user input'

    welcome()
    start = True
    while start:
        user_choice = input("Type A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        #   Viewing the calendar
        if user_choice == "V":
            #   Check for a non-empty calendar
            if len(calendar.keys()) < 1:
                print("Your calendar is empty.")
            else:
                print(calendar)
        #   Updating the calendar
        elif user_choice == "U":
            #   Check for a non-empty calendar
            if len(calendar.keys()) < 1:
                print("Your calendar is empty.")
                try_again = input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            #   If the calendar has events
            else:
                date = input("What date? ")
                update = input("Enter update: ")
                calendar[date] = update
                print("Update was successful.")
                print(calendar)
        #   Adding events to the calendar
        elif user_choice == "A":
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYYY): ")
            # Check for a valid date
            if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                print("The date provided is invalid. The event cannot take place in the past.")
                try_again = input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print("Event added.")
                print(calendar)
        #   Deleting events from the calendar
        elif user_choice == "D":
            #   Check for a non-empty calendar
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
        #   Exiting the calendar
        elif user_choice == "X":
            start = False
            print("The program is exiting. Goodbye.")
        #   Check for a valid command
        else:
            print("Invalid command. Exiting the program.")
            start = False
