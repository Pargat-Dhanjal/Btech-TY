import copy

EMPTY_SPACE = ' '
AI_MARKER = 'O'
PLAYER_MARKER = 'X'
WIN = 1
DRAW = 0
LOSS = -1
START_DEPTH = 0

winning_states = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(2, 0), (1, 1), (0, 2)]
]

def print_game_state(state):
    if state == WIN:
        print("AI wins!")
    elif state == DRAW:
        print("It's a draw!")
    elif state == LOSS:
        print("Player wins!")

def print_board(board):
    print()
    for row in board:
        print(row[0], '|', row[1], '|', row[2])
        print("----------")
    print()

def get_legal_moves(board):
    legal_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY_SPACE:
                legal_moves.append((i, j))
    return legal_moves

def position_occupied(board, pos):
    return board[pos[0]][pos[1]] != EMPTY_SPACE

def get_occupied_positions(board, marker):
    occupied_positions = []
    for i in range(3):
        for j in range(3):
            if marker == board[i][j]:
                occupied_positions.append((i, j))
    return occupied_positions

def board_is_full(board):
    for row in board:
        if EMPTY_SPACE in row:
            return False
    return True

def game_is_won(occupied_positions):
    for win_state in winning_states:
        if all(pos in occupied_positions for pos in win_state):
            return True
    return False

def get_opponent_marker(marker):
    return PLAYER_MARKER if marker == AI_MARKER else AI_MARKER

def get_board_state(board, marker):
    occupied_positions = get_occupied_positions(board, marker)
    opponent_marker = get_opponent_marker(marker)

    if game_is_won(occupied_positions):
        return WIN

    occupied_positions = get_occupied_positions(board, opponent_marker)
    if game_is_won(occupied_positions):
        return LOSS

    if board_is_full(board):
        return DRAW

    return DRAW

def minimax_optimization(board, marker, depth, alpha, beta):
    best_move = (-1, -1)
    best_score = LOSS if marker == AI_MARKER else WIN

    if board_is_full(board) or DRAW != get_board_state(board, AI_MARKER):
        best_score = get_board_state(board, AI_MARKER)
        return best_score, best_move

    legal_moves = get_legal_moves(board)
    for curr_move in legal_moves:
        board[curr_move[0]][curr_move[1]] = marker

        if marker == AI_MARKER: 
            score, _ = minimax_optimization(copy.deepcopy(board), PLAYER_MARKER, depth + 1, alpha, beta)
            best_score = max(best_score, score - depth)
            if best_score > alpha:
                alpha = best_score
                best_move = curr_move
            if beta <= alpha:
                break
        else:  
            score, _ = minimax_optimization(copy.deepcopy(board), AI_MARKER, depth + 1, alpha, beta)
            best_score = min(best_score, score + depth)
            if best_score < beta:
                beta = best_score
                best_move = curr_move
            if beta <= alpha:
                break

        board[curr_move[0]][curr_move[1]] = EMPTY_SPACE 

    return best_score, best_move

def game_is_done(board):
    return board_is_full(board) or DRAW != get_board_state(board, AI_MARKER)

def main():
    board = [[EMPTY_SPACE] * 3 for _ in range(3)]

    print("********************************\n\n\tTic Tac Toe AI\n\n********************************\n")
    print("Player = X\t AI Computer = O\n")
    print_board(board)

    while not game_is_done(board):
        row = int(input("Row (0-2): "))
        col = int(input("Column (0-2): "))
        print()

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Row and column should be between 0 and 2.")
            continue

        if position_occupied(board, (row, col)):
            print(f"The position ({row}, {col}) is occupied. Try another one...\n")
            continue

        board[row][col] = PLAYER_MARKER

        if game_is_done(board):
            print("Game Over")
            print_board(board)
            break

        best_score, best_move = minimax_optimization(copy.deepcopy(board), AI_MARKER, START_DEPTH, -float('inf'), float('inf'))
        board[best_move[0]][best_move[1]] = AI_MARKER

        print_board(board)

    result = get_board_state(board, AI_MARKER)
    print_game_state(result)

if __name__ == "__main__":
    main()
