import random
import sys

def generate_board(size, num_mines):
    """Generate the game board with the specified number of mines."""
    board = [[0 for _ in range(size)] for _ in range(size)]
    mines = set()

    while len(mines) < num_mines:
        mine = (random.randint(0, size - 1), random.randint(0, size - 1))
        if mine not in mines:
            mines.add(mine)
            x, y = mine
            board[x][y] = 'M'

            # Update numbers around the mine
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nx, ny = x + i, y + j
                    if 0 <= nx < size and 0 <= ny < size and board[nx][ny] != 'M':
                        if isinstance(board[nx][ny], int):
                            board[nx][ny] += 1

    return board, mines

def display_board(board, revealed):
    """Display the board to the user."""
    size = len(board)
    print("   " + " ".join([str(i) for i in range(size)]))
    print("  " + "--" * size)
    for i in range(size):
        row = []
        for j in range(size):
            if revealed[i][j]:
                row.append(str(board[i][j]))
            else:
                row.append(".")
        print(f"{i} | " + " ".join(row))

def reveal(board, revealed, x, y):
    """Reveal a cell and recursively reveal adjacent cells if the cell is empty."""
    if revealed[x][y]:
        return

    revealed[x][y] = True
    if board[x][y] == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if 0 <= nx < len(board) and 0 <= ny < len(board) and not revealed[nx][ny]:
                    reveal(board, revealed, nx, ny)

def check_victory(board, revealed):
    """Check if the player has won by revealing all non-mine cells."""
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 'M' and not revealed[i][j]:
                return False
    return True

def play_minesweeper(size=8, num_mines=10):
    """Main function to play the Minesweeper game."""
    board, mines = generate_board(size, num_mines)
    revealed = [[False for _ in range(size)] for _ in range(size)]

    while True:
        display_board(board, revealed)
        try:
            input_data = input("Enter coordinates to reveal (row col): ")
            if not input_data.strip():
                print("Input cannot be empty. Try again.")
                continue

            x, y = map(int, input_data.split())
            if not (0 <= x < size and 0 <= y < size):
                print("Invalid coordinates. Try again.")
                continue

            if board[x][y] == 'M':
                print("Boom! You hit a mine. Game Over.")
                display_board(board, [[True for _ in range(size)] for _ in range(size)])
                break

            reveal(board, revealed, x, y)

            if check_victory(board, revealed):
                print("Congratulations! You won!")
                display_board(board, [[True for _ in range(size)] for _ in range(size)])
                break

        except ValueError:
            print("Invalid input. Please enter row and column as numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Uncomment to play
# play_minesweeper()
