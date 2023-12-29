from collections import deque


class Node:
    def __init__(self, point, dist):
        self.point = point
        self.dist = dist

    def get_distance(self):
        return self.dist

    def get_point(self):
        return self.point


def get_valid_moves(grid, pos_i, pos_j):
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    valid_moves = []
    for delta in deltas:
        to_check_i = pos_i + delta[0]
        to_check_j = pos_j + delta[1]
        if 0 <= to_check_j < len(grid[pos_i]) and 0 <= to_check_i < len(grid):
            dest_elevation = ord(grid[to_check_i][to_check_j])
            source_elevation = ord(grid[pos_i][pos_j])
            if source_elevation - dest_elevation >= -1:
                valid_moves.append((to_check_i, to_check_j))
    return valid_moves


def get_shortest_path(start, grid):
    visited = []
    for i in range(len(grid)):
        visited.append([False] * len(grid[i]))

    queue = deque()
    queue.append(Node(start, 0))
    while queue:
        cur_node = queue.popleft()
        if cur_node.get_point()[0] == end[0] and cur_node.get_point()[1] == end[1]:
            return cur_node.get_distance()

        # add adjacent cells if there is a path
        next_moves = get_valid_moves(grid, cur_node.get_point()[0], cur_node.get_point()[1])
        for move in next_moves:
            if not visited[move[0]][move[1]]:
                visited[move[0]][move[1]] = True
                queue.append(Node(move, cur_node.get_distance() + 1))
    return 100000000


with open('../input/day12.txt', 'rt') as infile:
    lines = infile.readlines()
    grid = []
    start = None
    end = None
    all_lowest = []
    for i, line in enumerate(lines):
        if 'S' in line:
            start = (i, line.index('S'))
            line = line.replace('S', 'a')
        if 'E' in line:
            end = (i, line.index('E'))
            line = line.replace('E', 'z')
        grid.append(list(line.strip()))
        for j, val in enumerate(grid[i]):
            if val == 'a':
                all_lowest.append((i, j))

    dist = get_shortest_path(start, grid)
    print(f'Shortest distance from start {dist}')
    min_dist = 10000000
    for pos in all_lowest:
        dist = get_shortest_path(pos, grid)
        if dist < min_dist:
            min_dist = dist
    print(f'Shortest dist {min_dist}')
