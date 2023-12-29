with open('../input/day1.txt', 'r') as calfile:
    elves = []
    cur_inventory = []
    for line in calfile.readlines():
        line = line.strip()
        if '' == line:
            if len(cur_inventory) > 0:
                elves.append(cur_inventory)
                cur_inventory = []
        else:
            cur_inventory.append(int(line))
    sums = []
    for elf in elves:
        sums.append(sum(elf))
    print(f'max {max(sums)}')
    sums.sort(reverse=True)
    total = 0
    for i in range(3):
        total += sums[i]
    print(f'Sum of 3 largest {total}')
