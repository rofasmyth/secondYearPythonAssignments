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
            print("You have chosen column ", col, ".") # Confirm column.
            return col # Return exits loop and returns to chooseSeat() and createTicketNum() function below.

# Function to choose a seating row called by the chooseSeat() function.            
def chooseRow():
    # While loop for error checking and retries.
    while True:
        row = int(input("Please enter a row number or 0(zero) to return to main menu: "))
        if row == 0: # Escape clause.
            return 0 # Returns 0 to chooseSeat() function below.
        # Ensure selection between 1 and 8, available columns.
        if row > 5 or row < 1:
            print("Please choose a valid row between 1 and 5.")
        else:
            print("You have chosen row ", row, ".") # Confirm column.
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
        print("---------------------")
        print("Your ticket number is: " + ticketNum)
        print("---------------------")
        
    else: # If seat is already taken, displays error and exits to main menu.
        print("This seat is already taken. Please book a seat again.")

    

# This function checks if the user has a valid PIN and if so, calls the chooseSeat() function
# which in turn calls the other functions above.
def book():
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
