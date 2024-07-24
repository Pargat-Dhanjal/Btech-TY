from collections import deque

def print_board(board):
    for row in board:
        print(row)

def get_blank_position(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return (i, j)

def is_valid_move(i, j):
    return 0 <= i < 3 and 0 <= j < 3

def swap_tiles(board, blank_pos, new_pos):
    i1, j1 = blank_pos
    i2, j2 = new_pos
    board[i1][j1], board[i2][j2] = board[i2][j2], board[i1][j1]

def is_goal_state(board, goal_state):
    return board == goal_state

def get_neighbors(board):
    blank_pos = get_blank_position(board)
    neighbors = []

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for move in moves:
        new_pos = (blank_pos[0] + move[0], blank_pos[1] + move[1])
        if is_valid_move(*new_pos):
            new_board = [row.copy() for row in board]
            swap_tiles(new_board, blank_pos, new_pos)
            neighbors.append(new_board)

    return neighbors

def bfs_8_puzzle(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if is_goal_state(current_state, goal_state):
            return path + [current_state]

        if tuple(map(tuple, current_state)) not in visited:
            visited.add(tuple(map(tuple, current_state)))
            neighbors = get_neighbors(current_state)

            for neighbor in neighbors:
                queue.append((neighbor, path + [current_state]))

    return None

def dfs_8_puzzle(initial_state, goal_state):
    visited = set()
    stack = [(initial_state, [])]

    while stack:
        current_state, path = stack.pop()

        if is_goal_state(current_state, goal_state):
            return path + [current_state]

        if tuple(map(tuple, current_state)) not in visited:
            visited.add(tuple(map(tuple, current_state)))
            neighbors = get_neighbors(current_state)

            for neighbor in neighbors:
                stack.append((neighbor, path + [current_state]))

    return None

def dls_8_puzzle(initial_state, goal_state, max_depth):
    visited = set()
    stack = [(initial_state, [], 0)]

    while stack:
        current_state, path, depth = stack.pop()

        if depth > max_depth:
            continue

        if is_goal_state(current_state, goal_state):
            return path + [current_state]

        if tuple(map(tuple, current_state)) not in visited:
            visited.add(tuple(map(tuple, current_state)))
            neighbors = get_neighbors(current_state)

            for neighbor in neighbors:
                stack.append((neighbor, path + [current_state], depth + 1))

    return None



initial_state = [
    [8, 1, 3],
    [0, 2, 4],
    [7, 6, 5]
]

goal_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

solution = dls_8_puzzle(initial_state, goal_state,3)

if solution:
    print("Solution found:")
    for step in solution:
        print_board(step)
        print()
else:
    print("No solution found.")
