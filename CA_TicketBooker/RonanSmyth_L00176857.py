# Written By: Ronan Smyth_L00176857
# Desc: A program to
#                (1) Register a user.
#                (2) Book and cancel tickets.
#                (3) Display available seats, registered users and tickets bought.
#                (4) Search for ticket by user ID.
#                (5) Validate Tickets which are used.
# FileName: CA_RWC_TicketBookingSystem.py
# Date: 05/11/2023  

#---------Imports------------------------------------------------------------------------

from random import randint

#---------2D list(Grid)------------------------------------------------------------------

# 2D list initialised to represent the grid of empty or booked seats.
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

#---------Dictionaries------------------------------------------------------------------------

# I used 3 dictionaries for easy reference of stored information.
# Dictionary uniquePIN : Name
pinName = {}
# Dictionary uniquePIN : TicketNumber
pinAndTicket = {}
# Dictionary TicketNumber : isValid(True/False)
ticketAndIsValid = {}

#---------displaySeats()------------------------------------------------------------------------

# This funtion prints the numbered grid showing available and booked seats.
def displaySeats():
    print("------------------------------------------------------")
    
    # Print gap before start of numbering for columns to allow space for row numbers.
    print("    ", end="")
    # Print a number for each member of the first list in the 2D list, which represents the columns.
    for i in range(len(grid[0])):
        # Use i+1 to begin at 1 instead of zero and :2 spaces the numbers.
        print(f"{i + 1:2}", end=" ")
    print()
    # Prints a line seperating column numbers from the seats. *3 compensates for the spaces between the numbers while -1 removes the extra line.
    print("    " + "-" * (len(grid[0]) * 3 - 1))  

    # Print the grid with enumerate() providing row numbers.
    for i, row in enumerate(grid):
        # Again i+1 starts at number 1 and :2 spaces enteries seperating the numbers from seats this time with "|".
        print(f"{i + 1:2} |", end=" ")
        for element in row:
            print(element, end="  ")
        print()

#---------register()&generatePin()------------------------------------------------------------------------

# Creates a 4-digit PIN for the register function below.
def generatePin():
    pin = ""
    # While loop iterates until unique pin is created, ensures the pin is unique.
    while True:
        # For loop interates 4 times for each digit in the PIN.
        for i in range(4):
            x = str(randint(0,9)) #Uses randint() in range between 1 and 9 and casts as string.
            pin = pin + x # Concatinates each new digit to the PIN variable.
        if pin not in pinName: # Checks if the PIN is already in the pinName dictionary, i.e. is it unique?
            return pin # If unique, returns PIN and exits the while loop.

# Function records a unique PIN as ID and associates it with a user's name.
def register():
    print("------------------------------------------------------")
    fName = ""
    sName = ""
    # 2 while loops here provide error checking for the users' names ensuring the names are made only from letters.
    while True:
        # Enter first and second names seperately to encourage accuracy and reduce errors.
        fName = input("Please enter your first name or 0(zero) to exit: ")
        if fName.isalpha():
            while True:
                sName = input("Please enter your surname or 0(zero) to exit: ")
                if sName.isalpha():
                    name = fName + " " + sName # Concatinate first name and surname with a space between.
                    name = name.title() # Convert name to title case for consistency.
                    pin = generatePin() # Call to generatePin() function above and stores PIN.   
                    pinName[pin] = name # Create key:value entry in dictionary storing the PIN as the key and name as the value.
                    print("---------------------")
                    print(name + " your PIN is: " + pin + ".") # Display name and pin
                    print("---------------------")
                    break
                elif sName == "0":# Exit cluse
                    break
                else:
                    print("Please try again using only letters.") # Error message if name not alphabetic.
            break
        
        elif fName == "0": # Exit cluse
            break
        else:
            print("Please try again using only letters.") # Error message if name not alphabetic.

#---------booking system(5 functions)------------------------------------------------------------------------

# Function to choose a seating column called by the chooseSeat() function.
def chooseCol():
    # While loop for error checking and retries.
    while True:
        col = int(input("Please enter a column number or 0(zero) to return to main menu: ")) # Cast input as int.
        if col == 0: # Escape clause.
            return 0 # Returns 0 to chooseSeat() function below.
        # Ensure selection between 1 and 8, available columns.
        if col > 8 or col < 1:
            print("Please choose a valid column between 1 and 8.")
        else:
            print("----------------------------------")
            print("You have chosen column ", col, ".") # Confirm column.
            print("----------------------------------")
            return col # Return exits loop and returns to chooseSeat() and createTicketNum() function below.

# Function to choose a seating row called by the chooseSeat() function.            
def chooseRow():
    print("------------------------------------------------------")
    # While loop for error checking and retries.
    while True:
        row = int(input("Please enter a row number or 0(zero) to return to main menu: "))
        if row == 0: # Escape clause.
            return 0 # Returns 0 to chooseSeat() function below.
        # Ensure selection between 1 and 8, available columns.
        if row > 5 or row < 1:
            print("Please choose a valid row between 1 and 5.")
        else:
            print("----------------------------------")
            print("You have chosen row ", row, ".") # Confirm column.
            print("----------------------------------")
            return row # Return exits loop and returns to chooseSeat() and createTicketNum() function below.

# Function to create the overly complicated ticket number;) called by chooseSeat().
# Ticket number format: PrcddddX -  Check number X: d4 + 2d3 + 3d2 +4d1 + 5c + 6r.
def createTicketNum(row, col, pin):
    # d1 through 4 seperates the string pin into 4 single character parts.
    d4 = int(pin[3])
    d3 = int(pin[2])
    d2 = int(pin[1])
    d1 = int(pin[0])
    # Calculations to determine check number.
    x = abs((((d4 + 2*d3 + 3*d2 +4*d1 + 5*col + 6*row)%10)-10))
    if x == 10: # If x is 10 then it's already divisible by ten and won't require addition.
        x = 0
    ticketNum = "P" + str(row) + str(col) + pin + str(x) # Concatenated elements of string.
    pinAndTicket[pin] = ticketNum # Saves to dictionary pinAndTicket.
    return ticketNum # Returns to chooseSeat() below.
    
# Function shows available seats in grid to user, stores a row and column selection,
# marks the seat as unavailable in the grid and displays the ticket number.
# This function calls displaySeats(), chooseRow(), chooseCol() and createTicketNum().
def chooseSeat(pin):
    # This code displays seating grid and explains the meaning of symbols.
    print()
    displaySeats()
    print()
    print("Please choose a seat.\nAvailable seats are marked as 0 while those marked as X are unavailable.")
    print()

    # This code stores row and column selection returned from above functions.
    row = chooseRow()
    
    if row != 0: 
        col = chooseCol()
    # This refers to the escape clause above allowing a user to exit back to the menu
    # before choosing a row and avoiding the escape clause in the chooseCol() function.
    else: 
        return # Returns to main menu.
    
    # Code marks seat in grid as unavailable.
    if grid[row-1][col-1] == 0:
        grid[row-1][col-1] = "X"

        # Call to function to create ticket number.
        ticketNum = createTicketNum(row, col, pin)
        
        # Stores ticket number and whether valid or used in a dictionary.
        ticketAndIsValid[ticketNum] = True

        # Displays ticket number to user.
        print("----------------------------------")
        print("Your ticket number is: " + ticketNum)
        print("----------------------------------")
        
    else: # If seat is already taken, displays error and exits to main menu.
        print("------------------------------------------------------")
        print("This seat is already taken. Please book a seat again.")
        print("------------------------------------------------------")

    

# This function checks if the user has a valid PIN and if so, calls the chooseSeat() function
# which in turn calls the other functions above.
def book():
    print("------------------------------------------------------")
    print("Only registered users may book a ticket. Have you already registered?")
    pin = ""
    # Code repeats until correct Pin received or until user enters zero.
    while pin not in pinName:
        # Stores Pin input by user.
        pin = input("Please enter your unique 4-digit PIN number or 0(zero) to return to main menu: ")
        if pin == "0": # Exit clause 0 to exit.
            break
        elif pin in pinName:
            chooseSeat(pin) # Checks if PIN exists and if so begins the seat booking process.
        else:
            print("This is not a valid PIN number. Please try again.")

#---------cancel()------------------------------------------------------------------------

# Function to cancel a booking and mark the previously unavailable seat as available.
def cancel():
    print("------------------------------------------------------")
    # Reads and stores a user-entered ticket number.
    ticketNum = input("Please enter your ticket number: ")
    keysToDelete = [] # List to avoid error caused when iterating over a changing collection.

    # Checks that ticket number exists.
    if ticketNum not in pinAndTicket.values():
        print("This is not a valid ticket number. Please try again.")
    else:
        # Search pinAndTicket dictionary for ticket number (value).
        for key, value in pinAndTicket.items():
            if value == ticketNum:
                keysToDelete.append(key) # Add key corresponding to value to keysToDelete list.

        # Iterate through keysToDelete list.
        for key in keysToDelete:
            if key in pinAndTicket:
                del pinAndTicket[key] # Delete ticket number from pinAndTicket dictionary.
            if key in ticketAndIsValid:
                del ticketAndIsValid[key]# Delete ticket number from ticketAndIsValid dictionary.
              
             
            grid[int(ticketNum[1])-1][int(ticketNum[2])-1] = 0 # Mark previously unavailable seat as available.
            print("------------------------------------------------------")
            print("Ticket number " + ticketNum + " has been deleted.") # Display ticket number.
            print("------------------------------------------------------")
            
#---------Listing&Searching(3 functions)------------------------------------------------------------------------

# Function to list booked tickets.
# Function prints unique PIN: Ticket number as key: value from pinAndTicket dictionary.
def listBookedTickets():
    print("----------------------")
    for key, value in pinAndTicket.items():
        print(f" {key} : {value}")

# Function to list registered users.
# Function prints unique PIN: Name as key: value from pinName dictionary.
def listUsrDetails():
    print("----------------------")
    for key, value in pinName.items():
        print(f" {key} : {value}")

# Function to enter a unique PIN and search to see if a user exists or has booked a ticket.
def searchUsrId():
    print("------------------------------------------------------")
    targetPIN = input("Please enter a user PIN to search for their ticket number.") # Stores target PIN to search for. 
    booked = False # Variable to check if user has booked ticket.
    registered = False # Variable to check if user has booked ticket.

    # Iterates over pinAndTicket looking for a booking.
    for key, value in pinAndTicket.items():
        if targetPIN == key:
            print(f"{key} : {value}") # Prints booking if found.
            booked = True

    # Iterates over pinName to check if the user is perhaps registered but hasnt booked a ticket yet.
    for key, value in pinName.items():
        if targetPIN == key:
            registered = True

    # If clauses to desplay error messages in the event there is no booking or or user doesn't exist.
    if booked == False and registered == False:    
        print("This PIN does not exist.")
    elif booked == False and registered == True:
        print("This PIN exist and the user is registered but has not booked a ticket.")

#---------Ticket Validation------------------------------------------------------------------------

# Function searches for a ticket and checks whether it has already been used.
# Option for use at entry to stadium by ushers etc.
def validate():
    print("------------------------------------------------------")
    # Read ticket number.
    ticketToValidate = input("Please enter a ticket number to be validated.")
    found = False # Variable to verify if ticket exists.

    # Iterates over ticketAndIsValid dictionary which stores ticket Number: True or False as key:value.
    for key, value in ticketAndIsValid.items():
        if ticketToValidate == key:
            found = True # Ticket exists if found in dictionary ticketAndIsValid.
            if ticketAndIsValid[key] == True: # Check if ticket is valid (True).
                print("This ticket is valid.") # Display outcome.

                while True: # while ensures only Y or N as answers.
                    # Usher can mark ticket as used.
                    isValid = input("Do you want to mark this ticket as used? Enter Y for yes and N for no.")
                    valid = isValid.upper()
                    if valid == "Y":
                        ticketAndIsValid[key] = False # Invalidate ticket.
                        print("This ticket has been used and is now invalid.")
                        return # Exit to main menu.
                    elif valid == "N":
                        print("This ticket has not been used and is still valid.")
                        return # Exit to main menu.
                    else: # Advises user to try again.
                        print("Please make a valid entry. Press Y to invalidate ticket or N to exit.")
                        
            elif ticketAndIsValid[key] == False: # If ticket is not valid (False).
                print("This ticket is invalid.") # Display outcome.
                    
    if found == False:  # If ticket not found or doesn't exist.  
        print("This ticket number unfortunately does not exist.")

#---------The main program calling the functions------------------------------------------------------------------------   
            
while True:
    print()
    print("Rugby World Cup Booking System")
    print()
    print("1. Display All Tickets/Seats")
    print("2. Register")
    print("3. Book a Ticket")
    print("4. Cancel a Ticket")
    print("5. List All Tickets Booked")
    print("6. List details of all Registered Users")
    print("7. Search for ticket by user ID")
    print("8. Validate Ticket")

    print("0. Quit")
    print()
    print("Enter Zero[0] to Quit")

    selection = input("Please make a selection from the Menu: ")

    if selection == "1":
        displaySeats()
    elif selection == "2":
        register()
    elif selection == "3":
        book()
    elif selection == "4":
        cancel()
    elif selection == "5":
        listBookedTickets()
    elif selection == "6":
        listUsrDetails()
    elif selection == "7":
        searchUsrId()
    elif selection == "8":
        validate()
    elif selection == "0":
        print("Thank you! Goodbye!")
        break
    else:
        print("Please make a valid selection between 1 and 8 OR select 0(zero) to quit.")
    
    
        
