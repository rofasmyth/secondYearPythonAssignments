
# This funtion prints the numbered grid showing available and booked seats.
def displaySeats():
    print()
    
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
