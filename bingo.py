import random

def print_matrix(matrix):
    for row in matrix:
        print(row)

def game(element, computer, user):
    for i in range(len(computer)):
        for j in range(len(computer[i])):
            if computer[i][j] == element:
                computer[i][j] = 0  
    for i in range(len(user)):
        for j in range(len(user[i])):
            if user[i][j] == element:
                user[i][j] = 0 

    return computer, user

def counter(matrix):
    row = 0
    col = 0
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_rows):
        count = 0
        for j in range(num_cols):
            if matrix[i][j] == 0:
                count += 1
        if count == num_cols: 
            row += 1
  

    for i in range(num_cols):
        count = 0
        for j in range(num_rows):
            if matrix[j][i] == 0:
                count += 1
        if count == num_rows:  
            col += 1
    
    return row + col


matrix1 = random.sample(range(1, 26), 25)  
matrix2 = random.sample(range(1, 26), 25)  


computer = [matrix1[i:i+5] for i in range(0, len(matrix1), 5)]
user = [matrix2[i:i+5] for i in range(0, len(matrix2), 5)]


print_matrix(user)

count_user = 0
count_comp = 0
map = set()  

while count_user < 5 and count_comp < 5: 
    print_matrix(user)  
    user_input = input("Enter element: ")

  
    try:
        user_input = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

 
    if user_input not in map:
        map.add(user_input)
        computer, user = game(user_input, computer, user)
    else:
        print(f"Element {user_input} has already been selected. Choose a different one.")
        continue

    
    while True:
        computer_input = random.randint(1, 25)
        if computer_input not in map:  
            break

    map.add(computer_input)
    computer, user = game(computer_input, computer, user)

 
    count_user = counter(user)
    count_comp = counter(computer)

   
    print(f"User's score: {count_user}, Computer's score: {count_comp}")


if count_user > count_comp:
    print("You Win!")
else:
    print("You Lose!")
