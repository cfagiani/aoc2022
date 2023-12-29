MAXY = 400
MAXX = 1000


def build_board(with_floor=False):
    board = []
    for y in range(MAXY):
        row = []
        for x in range(MAXX):
            row.append('.')
        board.append(row)
    with open('../input/day14.txt', 'rt') as infile:
        global_max_y = 0
        for line in infile.readlines():
            point_strings = line.strip().split(' -> ')
            points = []
            for p in point_strings:
                parts = p.split(',')
                points.append((int(parts[0]), int(parts[1])))
                if int(parts[1]) > global_max_y:
                    global_max_y = int(parts[1])
            for i in range(len(points) - 1):
                if points[i][0] < points[i + 1][0]:
                    minx = points[i][0]
                    maxx = points[i + 1][0]
                else:
                    minx = points[i + 1][0]
                    maxx = points[i][0]
                if points[i][1] < points[i + 1][1]:
                    miny = points[i][1]
                    maxy = points[i + 1][1]
                else:
                    miny = points[i + 1][1]
                    maxy = points[i][1]
                for y in range(miny, maxy + 1):
                    for x in range(minx, maxx + 1):
                        board[y][x] = '#'
    if with_floor:
        for x in range(MAXX):
            board[2 + global_max_y][x] = '#'
    return board, (global_max_y + 2 if with_floor else None)


def add_sand(board, floor_level):
    sand_pos = (500, 0)
    stopped = False
    while sand_pos[1] < MAXY - 1:
        if board[sand_pos[1] + 1][sand_pos[0]] == '.':
            sand_pos = (sand_pos[0], sand_pos[1] + 1)
        elif board[sand_pos[1] + 1][sand_pos[0] - 1] == '.':
            sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)
        elif board[sand_pos[1] + 1][sand_pos[0] + 1] == '.':
            sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
        else:
            if board[sand_pos[1]][sand_pos[0]] != 'o':
                board[sand_pos[1]][sand_pos[0]] = 'o'
                stopped = True
            break
    return stopped


board, floor = build_board(False)

counter = 0
while add_sand(board, floor):
    counter += 1
print(f'Added {counter} units of sand')

board, floor = build_board(True)
counter = 0
while add_sand(board, floor):
    counter += 1
print(f'Added {counter} units of sand')
