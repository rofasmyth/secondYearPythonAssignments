# Function searches for a ticket and checks whether it has already been used.
# Option for use at entry to stadium by ushers etc.
def validate():
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
