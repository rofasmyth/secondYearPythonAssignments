# Function to cancel a booking and mark the previously unavailable seat as available.
def cancel():
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
            del pinAndTicket[key] # Delete ticket number from pinAndTicket dictionary.
            del ticketAndIsValid[key] # Delete ticket number from ticketAndIsValid dictionary.
            grid[int(ticketNum[1])-1][int(ticketNum[2])-1] = 0 # Mark previously unavailable seat as available.
            print("---------------------")
            print("Ticket number " + ticketNum + " has been deleted.") # Display ticket number.
            print("---------------------")
