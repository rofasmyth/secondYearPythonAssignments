# Creates a 4-digit PIN for the register function below.
def generatePin():
    # pin = ""
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
    fName = ""
    sName = ""
    # 2 while loops here provide error checking for the users' names ensuring the names are made only from letters.
    while True:
        # Enter first and second names seperately to encourage accuracy and reduce errors.
        fName = input("Please enter your first name or 0(zero) to exit: ")
        if fName.isAlpha():
            while True:
                sName = input("Please enter your surname or 0(zero) to exit: ")
                if sName.isAlpha():
                    name = fName + " " + sName # Concatinate first name and surname with a space between.
                    name = name.title() # Convert name to title case for consistency.
                    pin = generatePin() # Call to generatePin() function above and stores PIN.   
                    pinName[pin] = name # Create key:value entry in dictionary storing the PIN as the key and name as the value.
                    break
                elif sName == 0:
                    break
                else:
                    print("Please try again using only letters.")
            break
        
        elif fName == 0:
            break
        else:
            print("Please try again using only letters.")
            
    

    
