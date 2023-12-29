def visible_from_edge(i, j, forest, step):
    tree_height = forest[i][j]
    pos_i = i
    pos_j = j
    while True:
        pos_i = pos_i + step[0]
        pos_j = pos_j + step[1]
        if (0 > pos_i or pos_i >= len(forest)) or (0 > pos_j or pos_j >= len(forest[pos_i])):
            return True
        else:
            if forest[pos_i][pos_j] >= tree_height:
                return False


def get_view_distance(i, j, forest, step):
    tree_height = forest[i][j]
    pos_i = i
    pos_j = j
    count = 0
    while True:
        pos_i = pos_i + step[0]
        pos_j = pos_j + step[1]
        if (0 > pos_i or pos_i >= len(forest)) or (0 > pos_j or pos_j >= len(forest[pos_i])):
            return count
        else:
            if forest[pos_i][pos_j] < tree_height:
                count += 1
            else:
                count += 1
                return count


forest = []
with open('../input/day8.txt', 'rt') as infile:
    for line in infile.readlines():
        forest.append(list(line.strip()))

visible_count = 0
for i in range(0, len(forest)):
    for j in range(0, len(forest[i])):
        for step in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if visible_from_edge(i, j, forest, step):
                visible_count += 1
                break

print(f'Total Visible trees (part 1): {visible_count}')

max_score = 0
for i in range(0, len(forest)):
    for j in range(0, len(forest[i])):
        scores = []
        for step in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            scores.append(get_view_distance(i, j, forest, step))
        cur_score = 1
        for score in scores:
            cur_score *= score
        if cur_score > max_score:
            max_score = cur_score
print(f'Max scenic score (part 2): {max_score}')
