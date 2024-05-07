import matplotlib.pyplot as plt

# Sample state space tree data
state_space_tree = {
    (1, 2, 3): [(4, 5, 6), (7, 8, 9)],
    (4, 5, 6): [(10, 11, 12)],
    (7, 8, 9): [(13, 14, 15)],
    (10, 11, 12): [],
    (13, 14, 15): []
}

def draw_state_space_tree(tree, parent=None, depth=0, pos=None):
    if pos is None:
        pos = {parent: (0, 0)} if parent is not None else {}

    for child in tree[parent]:
        pos[child] = (depth, pos[parent][1] - 1)
        plt.plot([pos[parent][0], pos[child][0]], [pos[parent][1], pos[child][1]], 'bo-')
        draw_state_space_tree(tree, child, depth + 1, pos)

    for node, (x, y) in pos.items():
        plt.text(x, y, str(node), ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5))

    plt.xlabel('Depth')
    plt.ylabel('Height')
    plt.title('State Space Tree')
    plt.gca().invert_yaxis()
    plt.show()

# Visualize the state space tree
draw_state_space_tree(state_space_tree)
