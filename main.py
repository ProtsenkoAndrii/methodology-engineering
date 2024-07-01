from enum import Enum


class Player(Enum):
    BLACK = 1  # black
    WHITE = 2  # white


def check_win(board, stone):
    winning_count = 5
    n = len(board)
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == stone:
                for direction in directions:
                    count = 0
                    x, y = i, j
                    while 0 <= x < n and 0 <= y < n and board[x][y] == stone:
                        count += 1
                        x += direction[0]
                        y += direction[1]
                    if count == winning_count:
                        return True, i + 1, j + 1  # Return 1-based position
    return False, -1, -1


def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))


def main():
    board_size = 19

    board = [[0] * board_size for _ in range(board_size)]
    current_player = Player.BLACK
    move_count = 0

    while True:
        print_board(board)
        row = int(input(f"Player {current_player.value}, enter the row (1-{board_size}): ")) - 1
        col = int(input(f"Player {current_player.value}, enter the column (1-{board_size}): ")) - 1

        if board[row][col] == 0:
            board[row][col] = current_player.value
            move_count += 1

            win, win_row, win_col = check_win(board, current_player.value)
            if win:
                print_board(board)
                print(f"Player {current_player.value} wins!")
                print(f"Winning move starts at row {win_row}, column {win_col}")
                break

            if move_count == board_size * board_size:
                print("The game is a draw!")
                break

            current_player = Player.WHITE if current_player == Player.BLACK else Player.BLACK
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    main()

