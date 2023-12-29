def process_move(line, stacks, preserve_order=False):
    parts = line.split(" from ")
    qty = parts[0].split("move ")[1]
    coords = parts[1].split(" to ")
    source = stacks[int(coords[0]) - 1]
    dest = stacks[int(coords[1]) - 1]
    if preserve_order:
        for i in range(int(qty), 0, -1):
            dest.insert(0, source.pop(i - 1))
    else:
        for i in range(int(qty)):
            dest.insert(0, source.pop(0))


def process_stacks(preserve_order):
    with open('../input/day5.txt', 'rt') as infile:
        stacks = []
        found_idx = False
        for line in infile.readlines():
            cur_line_arr = list(line)
            if len(line.strip()) == 0:
                continue
            if len(stacks) == 0:
                for i in range(int((len(line) - 1) / 3)):
                    stacks.append([])
            if not line.strip().startswith('1') and not found_idx:
                idx = -1
                for pos in range(0, len(cur_line_arr), 4):
                    idx += 1
                    if ' ' != cur_line_arr[pos + 1]:
                        stacks[idx].append(cur_line_arr[pos + 1])
            else:
                found_idx = True

            if found_idx and line.strip().startswith('1'):
                continue
            elif found_idx:
                process_move(line, stacks, preserve_order)
        for stack in stacks:
            print(stack[0])


print('One at a time:')
process_stacks(False)
print('Preserving order')
process_stacks(True)
