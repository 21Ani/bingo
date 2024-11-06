# bingo
This is a simple Bingo Game implementation using Python. In this game, the user plays against the computer on a 5x5 Bingo grid, and both players mark off numbers on their boards. The first player to complete five numbers in a row (either horizontally, vertically, or diagonally) wins the game.

**Features:**
1. The game is played on two 5x5 grids: one for the user and one for the computer.
2. Both players take turns to choose a number between 1 and 25.
3. If the number is on the grid, it gets marked as 0.
4. The game tracks the number of rows and columns that are fully marked off for both players (i.e., rows/columns where all values are 0).
5. The game ends when one player completes 5 rows or columns (Bingo), and the other player loses.
   
**How to Play:**
1. The game generates a random Bingo grid for both the user and the computer.
2. The user is prompted to enter a number between 1 and 25.
3. The computer randomly selects a number that hasn't been chosen yet.
4. The game continues with each player marking off numbers on their grid.
5. The game ends when either the user or the computer completes 5 rows or columns.
