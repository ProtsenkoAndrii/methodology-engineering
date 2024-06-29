def check_win(board, stone):
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
                    if count == 5:
                        return True, i + 1, j + 1  # Return 1-based position
    return False, -1, -1


def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))


def main():
    import sys

    board = [[0] * 19 for _ in range(19)]
    current_player = 1  # 1 - black, 2 - white
    move_count = 0

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (1-19): ")) - 1
        col = int(input(f"Player {current_player}, enter the column (1-19): ")) - 1

        if board[row][col] == 0:
            board[row][col] = current_player
            move_count += 1

            win, win_row, win_col = check_win(board, current_player)
            if win:
                print_board(board)
                print(f"Player {current_player} wins!")
                print(f"Winning move starts at row {win_row}, column {win_col}")
                break

            if move_count == 19 * 19:
                print("The game is a draw!")
                break

            current_player = 2 if current_player == 1 else 1
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    main()
