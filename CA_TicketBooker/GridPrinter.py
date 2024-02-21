grid = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Print column numbers
print("    ", end="")
for i in range(len(grid[0])):
    print(f"{i + 1:2}", end=" ")
print()
# Print the line
print("    " + "-" * (len(grid[0]) * 3 - 1))  # Adjust the length of the line as needed

# Print the grid with row numbers
for i, row in enumerate(grid):
    print(f"{i + 1:2} |", end=" ")
    for element in row:
        print(element, end="  ")
    print()
