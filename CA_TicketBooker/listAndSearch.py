# Function to list booked tickets.
# Function prints unique PIN: Ticket number as key: value from pinAndTicket dictionary.
def listBookedTickets():
    for key, value in pinAndTicket.items():
        print(f" {key} : {value}")

# Function to list registered users.
# Function prints unique PIN: Name as key: value from pinName dictionary.
def listUsrDetails():
    for key, value in pinName.items():
        print(f" {key} : {value}")

# Function to enter a unique PIN and search to see if a user exists or has booked a ticket.
def searchUsrId():
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
