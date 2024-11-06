import random  # Importing the random module to generate random numbers

# Function to print a matrix (5x5 grid)
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Function to update the matrix when a player picks a number
def game(element, computer, user):
    # Update the computer's matrix: mark selected element as 0
    for i in range(len(computer)):
        for j in range(len(computer[i])):
            if computer[i][j] == element:
                computer[i][j] = 0  # Mark the element as 0
    
    # Update the user's matrix: mark selected element as 0
    for i in range(len(user)):
        for j in range(len(user[i])):
            if user[i][j] == element:
                user[i][j] = 0  # Mark the element as 0 

    return computer, user  # Return the updated matrices

# Function to count the number of rows and columns with all elements marked (i.e., 0)
def counter(matrix):
    row = 0  # Variable to count the number of completed rows
    col = 0  # Variable to count the number of completed columns
    num_rows = len(matrix)  # Get the number of rows in the matrix
    num_cols = len(matrix[0])  # Get the number of columns in the matrix

    # Check completed rows
    for i in range(num_rows):
        count = 0  # Counter for the number of 0's in the row
        for j in range(num_cols):
            if matrix[i][j] == 0:  # If the element is 0 (marked)
                count += 1
        if count == num_cols:  # If the row is completely marked
            row += 1  # Increment the row count

    # Check completed columns
    for i in range(num_cols):
        count = 0  # Counter for the number of 0's in the column
        for j in range(num_rows):
            if matrix[j][i] == 0:  # If the element is 0 (marked)
                count += 1
        if count == num_rows:  # If the column is completely marked
            col += 1  # Increment the column count
    
    return row + col  # Return the total number of completed rows and columns

# Generate two random lists of 25 numbers for the computer and user (values from 1 to 25)
matrix1 = random.sample(range(1, 26), 25)  
matrix2 = random.sample(range(1, 26), 25)  

# Create a 5x5 matrix for both the computer and user
computer = [matrix1[i:i+5] for i in range(0, len(matrix1), 5)]
user = [matrix2[i:i+5] for i in range(0, len(matrix2), 5)]

# Print the user's matrix at the beginning
# print_matrix(user)

# Initialize scores for both players
count_user = 0
count_comp = 0

# Create a set to track the numbers already selected by both players
map = set()  

# The game continues until either player has 5 completed rows/columns
while count_user < 5 and count_comp < 5: 
    # Print the user's current matrix
    print_matrix(user)  
    
    # Prompt the user to enter a number
    user_input = input("Enter element: ")

    # Validate that the input is an integer
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue  # If invalid, ask the user to input a number again

    # Check if the user has already selected this number
    if user_input not in map:
        map.add(user_input)  # Add the number to the set of selected numbers
        # Update both matrices (user and computer) based on the user's selection
        computer, user = game(user_input, computer, user)
    else:
        print(f"Element {user_input} has already been selected. Choose a different one.")
        continue  # If the number has already been selected, ask for a new one

    # Computer's turn: randomly select a number from 1 to 25
    while True:
        computer_input = random.randint(1, 25)
        if computer_input not in map:  # Ensure the computer doesn't pick a number already chosen
            break

    map.add(computer_input)  # Add the computer's number to the selected numbers
    # Update both matrices (user and computer) based on the computer's selection
    computer, user = game(computer_input, computer, user)

    # Count the number of completed rows/columns for both the user and the computer
    count_user = counter(user)
    count_comp = counter(computer)

    # Print the current scores
    print(f"User's score: {count_user}, Computer's score: {count_comp}")

# Determine and print the winner based on the scores
if count_user > count_comp:
    print("You Win!")
else:
    print("You Lose!")
