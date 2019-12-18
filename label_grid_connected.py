grid = [[1, 0, 0],
        [1, 1, 1],
        [0, 1, 0],
        [0, 1, 1],
        [0, 1, 0],
        [0, 0, 0]]

def label(grid):
    height = len(grid)
    width = len(grid[0])
    to_visit = set(((i, j) for i in range(height) for j in range(width)))
    labels = [[None for j in range(width)] for i in range(height)]
    label_idx = 1
    while to_visit:
        coord = to_visit.pop()
        connected = dfs(grid, coord, labels, label_idx)
        label_idx += 1
        to_visit = to_visit - set(connected)
    return labels

def dfs(grid, coord, labels, label):
    height = len(grid)
    width = len(grid[0])
    offsets = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    visited = []
    to_visit = [coord]
    while to_visit:
        coord = to_visit.pop()
        x, y = coord
        if (0 <= x < height) and (0 <= y < width):
            if grid[x][y] == 0:
                labels[x][y] = label
                for coord_off in offsets:
                    new_coord = (x + coord_off[0], y + coord_off[1])
                    if new_coord not in visited:
                        to_visit.append(new_coord)
        visited.append(coord)
    return visited


def convert(val):
    if val is None:
        return 0
    else:
        return val

def grid_print(grid):
    print("====")
    for row in grid:
        print([convert(val) for val in row])
    print("====")

print("input")
grid_print(grid)
print("output")
grid_print(label(grid))
