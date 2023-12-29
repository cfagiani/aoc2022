def get_score(moves):
    if moves[0] == 'A':
        # ROCK
        if moves[1] == 'Y':
            return 6 + 2
        elif moves[1] == 'X':
            return 3 + 1
        else:
            return 3
    elif moves[0] == 'B':
        # PAPER
        if moves[1] == 'Z':
            return 6 + 3
        elif moves[1] == 'Y':
            return 3 + 2
        else:
            return 1
    elif moves[0] == 'C':
        # SCISSOR
        if moves[1] == 'X':
            return 6 + 1
        elif moves[1] == 'Z':
            return 3 + 3
        else:
            return 2


def convert_move(moves):
    if moves[0] == 'A':
        # ROCK
        if moves[1] == 'X':
            return ['A', 'Z']
        elif moves[1] == 'Y':
            return ['A', 'X']
        else:
            return ['A', 'Y']
    elif moves[0] == 'B':
        # PAPER
        if moves[1] == 'X':
            return ['B', 'X']
        elif moves[1] == 'Y':
            return ['B', 'Y']
        else:
            return ['B', 'Z']
    elif moves[0] == 'C':
        # SCISSOR
        if moves[1] == 'X':
            return ['C', 'Y']
        elif moves[1] == 'Y':
            return ['C', 'Z']
        else:
            return ['C', 'X']


with open('../input/day2.txt', 'r') as stratfile:
    total = 0
    for line in stratfile:
        total += get_score(line.strip().split(' '))
    print(f'total score {total}')

with open('../input/day2.txt') as stratfile:
    total = 0
    for line in stratfile:
        total += get_score(convert_move(line.strip().split(' ')))
    print(f'alternate score {total}')
