# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Ensure the user entered a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize the row counter
    row = 0

    # Use a while loop to iterate through each row
    while row < size:
        # Use a for loop to print asterisks in each row
        for col in range(size):
            print("*", end="")
        # Print a newline character to move to the next row
        print()
        # Increment the row counter
        row += 1

