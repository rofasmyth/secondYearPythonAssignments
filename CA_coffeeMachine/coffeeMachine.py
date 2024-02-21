## Written by: Ronan Smyth
## Student No: L00176857
## Date: 20/12/2023
## Description: CA3 - in class exam. A coffe machine class to manage the use of a coffee machine.
## Filename: coffeeMachine.py

class CoffeeMachine():
    
    # Constructor for objects of the coffee machine class.
    # Default water and beans levels set to zero but changeable through the arguments.
    # _numEspressosMade attribute set to zero on instantiation of coffee machine object.
    def __init__(self, beansLevel = 0.0, waterLevel = 0.0):
        self._beansLevel = beansLevel
        self._waterLevel = waterLevel
        self._numEspressosMade = 0

    # A method to add or refill coffee beans in the coffee machine.
    def addBeans(self, beansIn):
        self._beansLevel = self._beansLevel + beansIn

    # A method to add or refill water in the coffee machine. 
    def addWater(self, waterIn):
        self._waterLevel = self._waterLevel + waterIn

    # Getter methods returning beans, water and number of coffees made (respectively).
    def getBeansLevel(self):
        return self._beansLevel

    def getWaterLevel(self):
        return self._waterLevel

    def getNumEspressosMade(self):
        return self._numEspressosMade 

    # A method to increase the count of coffees made while decreasing the amount of coffee beans and water in the machine.
    # Error checking takes place below, as commented, to ensure a coffee cannot be made while insufficient levels of either beans or water are present.
    def makeEspresso(self):
        if (self._beansLevel >= 7.5 and self._waterLevel >= 30): # Check that sufficient levels of beans and water are present.
            self._beansLevel = self._beansLevel - 7.5 # Decrease amount of beans for 1 espresso.
            self._waterLevel = self._waterLevel - 30 # Decrease amount of water for 1 espresso.
            self._numEspressosMade = self._numEspressosMade + 1 # Increase the counter for number of coffees made.
            print("Espresso ready.")
        else:
            if (self._beansLevel < 7.5 and self._waterLevel < 30): 
                print("Insufficient coffee beans and water to make an espresso.") # Error message if both beans and water levels are insufficient.
            elif (self._beansLevel < 7.5):
                print("Insufficient coffee beans to make an espresso.") # Error message if beans level insufficient.
            elif (self._waterLevel < 30):
                print("Insufficient water to make an espresso.") # Error message if water level insufficient.

    # A method to empty beans and water levels and reset coffees-made counter to zero.          
    def emptyMachine(self):
        self._beansLevel = 0
        self._waterLevel = 0
        self._numEspressosMade = 0
        print("Machine has been emptied.")

    # A method to return a string represention of the status of the machine.
    # Note: I tried to use the ternary operator here but was unable to get it working.
    # Note: I used the .format() string method here and f-string for the __repr__().
    def __str__(self):
        if (self.getBeansLevel()<50 and self.getWaterLevel()<90):
            return "Water Level: {}ml | Coffee beans level: {}g | No. of coffees made: {} | Coffee low | Water low ".format(self.getWaterLevel(), self.getBeansLevel(), self.getNumEspressosMade() )
        elif (self.getBeansLevel()<50):
            return "Water Level: {}ml | Coffee beans level: {}g | No. of coffees made: {} | Coffee low ".format(self.getWaterLevel(), self.getBeansLevel(), self.getNumEspressosMade() )
        elif (self.getWaterLevel()<90):
            return "Water Level: {}ml | Coffee beans level: {}g | No. of coffees made: {} | Water low ".format(self.getWaterLevel(), self.getBeansLevel(), self.getNumEspressosMade() )
        else:
            return "Water Level: {}ml | Coffee beans level: {}g | No. of coffees made: {}".format(self.getWaterLevel(), self.getBeansLevel(), self.getNumEspressosMade() ) 

    # A method to return a string representation for developers which can be used to recreate or create a duplicate of the object.
    def __repr__(self):
        return f"CoffeeMachine({self.getBeansLevel()}, {self.getWaterLevel()})"


# Tester program for the above class and objects thereof.
def main():
    
    print("=======================================================")
    print("Instantiate object, add and getter methods")
    machine1 = CoffeeMachine() # Checks that an object can be instantiated.
    machine1.addBeans(1000) # Checks that beans can be added to the machine.
    machine1.addWater(5000) # Checks that water can be added to the machine.
    print("Beans Level: ", machine1.getBeansLevel() ) # Checks getBeansLevel() method.
    print("Water Level: ", machine1.getWaterLevel() ) # Checks getWaterLevel() method.
    print("No. of espressos made: ", machine1.getNumEspressosMade() ) # Checks getNumEspressosMade() method.

    print("=======================================================")
    print("Make 3 espressos =>")
    machine1.makeEspresso()
    machine1.makeEspresso()
    machine1.makeEspresso() # Checks that espressos can be made.
    print("New Beans Level: ", machine1.getBeansLevel() ) # Checks that beans level decreases by the correct amount: 22.5g
    print("New water Level: ", machine1.getWaterLevel() ) # Checks that water level decreases by the correct amount: 90ml
    print("No. of espressos made: ", machine1.getNumEspressosMade() ) # Checks that coffee counter attribute increases by 3.

    print("=======================================================")
    print("Empty the machine =>")
    machine1.emptyMachine() # Check that machine empties correctly: Levels and counter to zero.
    print("Empty Beans Level: ", machine1.getBeansLevel() ) # Checks that beans level empties: 0g
    print("Empty water Level: ", machine1.getWaterLevel() ) # Checks that water level empties: 0ml
    print("No. of espressos made: ", machine1.getNumEspressosMade() ) # Checks that coffee counter attribute is reset to zero.

    print("=======================================================")
    print("Error checking =>")
    machine1.makeEspresso() # What error when coffee made with empty machine?: Insufficient coffee beans and water to make an espresso.
    machine1.addBeans(1000)
    machine1.makeEspresso() # What error when coffee made with no water in machine?: Insufficient water to make an espresso.
    machine1.emptyMachine()
    machine1.addWater(5000) 
    machine1.makeEspresso() # What error when coffee made with no beans in machine?: Insufficient coffee beans to make an espresso.

    print("=======================================================")
    print("Test str()")
    machine1.addBeans(1000) # Add beans so as not to print either of the warnings: ' | Coffee low | Water low '.
    print(machine1)
    machine1.emptyMachine() # Empty machine to check that it prints both warnings: ' | Coffee low | Water low '.
    print(machine1)
    machine1.addBeans(1000) # Add beans so as not to print the warnings: ' | Coffee low '.
    print(machine1)
    machine1.emptyMachine()
    machine1.addWater(5000) # Add only water to check only the warnings: ' | Coffee low '.
    print(machine1)

    print("=======================================================")
    print("Test repr()")
    print(repr(machine1)) # Check that the repr() could be used to create a duplicate object.
    

main()
        
