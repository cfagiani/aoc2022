def get_priority(ltr):
    if ltr.isupper():
        return ord(ltr) - 64 + 26
    else:
        return ord(ltr) - 96


with open('../input/day3.txt', 'rt') as infile:
    total = 0
    for line in infile.readlines():
        contents = list(line.strip())
        compartments = [contents[0:int(len(contents) / 2)], contents[int(len(contents) / 2):]]
        for ltr in compartments[0]:
            if ltr in compartments[1]:
                total += get_priority(ltr)
                break
    print(f'Sum of priorities {total}')

with open('../input/day3.txt', 'rt') as infile:
    total = 0
    lines = infile.readlines()
    for i in range(0, len(lines), 3):
        for ltr in list(lines[i]):
            if ltr in lines[i + 1] and ltr in lines[i + 2]:
                total += get_priority(ltr)
                break

print(f'Sum of badge priorities {total}')
