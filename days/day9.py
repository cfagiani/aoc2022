import operator


def move_snake(snake):
    tail_visits = {(0, 0): 1}
    with open('../input/day9.txt', 'rt') as infile:
        for line in infile.readlines():
            parts = line.strip().split(' ')
            for i in range(0, int(parts[1])):
                if parts[0] == 'R':
                    delta = (1, 0)
                elif parts[0] == 'L':
                    delta = (-1, 0)
                elif parts[0] == 'U':
                    delta = (0, 1)
                else:
                    delta = (0, -1)
                snake[0] = (snake[0][0] + delta[0], snake[0][1] + delta[1])
                for j in range(1, len(snake)):
                    knot_distance = tuple(map(operator.sub, snake[j - 1], snake[j]))
                    # more than 1 away, need to move
                    if (knot_distance[0] == 1 and knot_distance[1] == 2) or (
                            knot_distance[0] == 2 and knot_distance[1] == 1) or (
                            knot_distance[0] == 2 and knot_distance[1] == 2):
                        # diagonal up, right
                        snake[j] = (snake[j][0] + 1, snake[j][1] + 1)
                    elif (knot_distance[0] == 1 and knot_distance[1] == -2) or (
                            knot_distance[0] == 2 and knot_distance[1] == -1) or (
                            knot_distance[0] == 2 and knot_distance[1] == -2):
                        # diagonal down, right
                        snake[j] = (snake[j][0] + 1, snake[j][1] - 1)
                    elif (knot_distance[0] == -1 and knot_distance[1] == 2) or (
                            knot_distance[0] == -2 and knot_distance[1] == 1) or (
                            knot_distance[0] == -2 and knot_distance[1] == 2):
                        # diagonal up, left
                        snake[j] = (snake[j][0] - 1, snake[j][1] + 1)
                    elif (knot_distance[0] == -1 and knot_distance[1] == -2) or (
                            knot_distance[0] == -2 and knot_distance[1] == -1) or (
                            knot_distance[0] == -2 and knot_distance[1] == -2):
                        # diagonal down, left
                        snake[j] = (snake[j][0] - 1, snake[j][1] - 1)
                    elif knot_distance[0] == 2:
                        snake[j] = (snake[j][0] + 1, snake[j][1])
                    elif knot_distance[0] == -2:
                        snake[j] = (snake[j][0] - 1, snake[j][1])
                    elif knot_distance[1] == 2:
                        snake[j] = (snake[j][0], snake[j][1] + 1)
                    elif knot_distance[1] == -2:
                        snake[j] = (snake[j][0], snake[j][1] - 1)

                visit_count = tail_visits.get(snake[-1], 0)
                tail_visits[snake[-1]] = visit_count + 1
    print(f'Total positions tail visited {len(tail_visits)}')


print('2 knot snake')
move_snake([(0, 0)] * 2)
print('10 knot snake')
move_snake([(0, 0)] * 10)
