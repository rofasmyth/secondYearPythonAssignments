#Bank Account Class
class bankAccount:

    #Bank Account Constructor
    #Attributes - account_no, balance
    def __init__(self,account_no,balance,account_type):
        self.account_type = account_type
        self.account_no = account_no
        self.balance = balance
        self.accounts = []

    def create_account(self,account_no,balance,account_type):
        try:
            #Error handling - ensures correct values are entered for account_no & balance
            if account_no < 0 and balance < 0:
                print("Account Number and Balance must be a positive integer")
            elif not isinstance(account_no,int) or not isinstance(balance,float):
                raise TypeError("Account number and balance must be integers")
            
            
            if account_type == 'checking':
                self.account = checking_account(account_no,balance,account_type)
            elif account_type == 'savings':
                self.account = savings_account(account_no,balance,account_type)
            else:
                print("Invalid account type.Choose 'savings' or 'checking'")
                return

                # # #Intialise account_no & balance
                # # self.account_no = account_no
                # # self.balance = balance

                # #empty list to store bank account objects
                
                # #Intialises each bankAccount object
                # account = bankAccount(account_no,balance)
                # #append account objects to accounts
            self.accounts.append(self.account)
        except ValueError as e:
            print(f"Error: {e}")

    def get_account(self,account_no):
        for account in self.accounts:
            if account.account_no == account_no:
                return account

        print("Account not found")
        return None

    def __str__(self):
        return f"Account Type: {self.account_type} \nAccount Number: {self.account_no} \nAccount Balance: {self.balance}"
            
        


    #Deposit method
    #Attributes - amount
    def deposit(self,amount):
        try:
            #Ensures amount entered is a positive integer
            if amount < 0:
                raise ValueError("Depsoit amount must be positive")
            else:
                #adds amount to balance
                self.balance += amount
        except ValueError as e:
            print(f"Error: {e}")

    #withdraw method
    #Attribute - amount
    def withdraw(self,amount):
        try:
            #checks if amount greater than balance
            #Displays insufficient funds if condition is true
            if amount > self.balance:
                raise ValueError("Insufficient funds")
            #checks if amount entered is a positive integer
            #displays error message if condition is true 
            elif amount < 0:
                raise ValueError("Withdrawal amount must be positive")
            #takes the amount value from the balance
            else:
                self.balance -= amount
        except ValueError as e:
            print(f"Error: {e}")

    #getBalance method
    #returns the balance to the user
    def get_balance(self):
        return self.balance

# #Testing bankAccount class 
# print("bankAccount class tester")

# #bankAccount constructor test
# account = bankAccount(4567,1000)

# #Testing deposit method
# account.deposit(200)
# print(f"Account Balance: ${account.get_balance()}")

# #Test withdraw method
# account.withdraw(400)
# print(f"Account Balance: ${account.get_balance()}")

#Savings Account Class 
class savings_account(bankAccount):

    #savings_account constructor
    def __init__(self, account_no, balance,account_type):
        #Error handling - ensures correct values are entered for account_no & balance
        if account_no < 0 and balance < 0:
            print("Account Number and Balance must be a positive integer")
        else:
            #Intialises savings account
            super().__init__(account_no, balance,account_type)
    
    #addInterest method - calculates and adds interest rate to balance
    def add_interest(self):
        #Intialises interest_rate to 0.03
        interest_rate = 0.03
        #calculates value based on interest rate
        temp = self.balance * interest_rate
        #adds interest value to balance
        self.balance += temp

# #SavingsAccount tester
# print("savingsAccount class tester")
# #savings_account constructor test
# savings = savings_account(6374,100)

# print(f"Amount before interest added: ${savings.get_balance()}")
# savings.add_interest()#add_interest method test
# print(f"Amount after interest rate added: ${savings.get_balance()}")

#Checking Account class
class checking_account(bankAccount):

    #Constructor for checking account
    def __init__(self, account_no, balance,account_type):
        #Error handling - ensures correct values are entered for account_no & balance
        if account_no < 0 and balance < 0:
            print("Account Number and Balance must be a positive integer")
        else:
            super().__init__(account_no, balance,account_type)

    #overrided withdraw method - incorporates the withdraw limit      
    def withdraw(self,amount):
        withdrawal_limit = 250

        if amount > self.balance:
            return print(f"Insufficient funds ${self.balance}")
        elif amount > withdrawal_limit:
            return print(f"Max limit per transaction ${withdrawal_limit}")
        else:
            self.balance -= amount

    # def __str__(self):
    #     return 
        
# #Testing checking account class       
# print("checking_account tester")

# #checking_account constructor test
# account = checking_account(6347,100)

# #test withdraw when amount > balance
# account.withdraw(150)
# #test withdraw when amount
# account.deposit(500)
# account.withdraw(300)

def main():

    bank_account = bankAccount(0,0,None)

    while True:
        try:
            print("\nATM Menu")
            print("1. Check Account Details")
            print("2. Check Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Create Account")

            choice = input("Enter your choice: ")

            if choice == '1':
                account_no = int(input("Enter account number: "))
                account = bank_account.get_account(account_no)
                if account:
                    account_details = str(account)
                    print("Account Details: ")
                    print (account_details)
            elif choice == '2':
                account_no = int(input("Enter account number: "))
                account = bank_account.get_account(account_no)
                if account:
                    print(f"Account Balance: ${account.get_balance()}")
            elif choice == '3':
                account_no = int(input("Enter account number: "))
                account = bank_account.get_account(account_no)
                if account:
                    amount = float(input("Enter the amount you would like to deposit: "))
                    account.deposit(amount)
            elif choice == '4':
                account_no = int(input("Enter account number: "))
                account = bank_account.get_account(account_no)
                if account:
                    amount = float(input("Enter the amount you would like to withdraw: "))
                    account.withdraw(amount)
            elif choice == '5':
                account_no = int(input("Enter account number: "))
                balance = float(input("Enter the inital balance: "))
                account_type = input("Enter the account type (checking/savings)").lower()
                bank_account.create_account(account_no,balance,account_type)
                print("Account created succesfully.")
                
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid input. Please choose a number 1-6")
        except (TypeError,ValueError):
            print("Error! Invalid input")


if __name__ == "__main__":
    main()
        




       
