grid = [
    [0, 0, 'X', 'X', 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 'X', 'X', 'X'],
    [0, 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Print column numbers
print("    ", end="")
for i in range(len(grid[0])):
    print(f"{i + 1:2}", end=" ")
print()
# Print the line
print("    " + "-" * (len(grid[0]) * 3))  # Adjust the length of the line as needed
