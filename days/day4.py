def extract_range(range_string):
    parts = range_string.split("-")
    return (int(parts[0]), int(parts[1]))


with open('../input/day4.txt', 'rt') as infile:
    total_contain_count = 0
    any_overlap_count = 0
    for line in infile.readlines():
        pairing = line.strip().split(',')
        rangeA = extract_range(pairing[0])
        rangeB = extract_range(pairing[1])
        if rangeA[0] <= rangeB[0] and rangeA[1] >= rangeB[1]:
            total_contain_count += 1
        elif rangeA[0] >= rangeB[0] and rangeA[1] <= rangeB[1]:
            total_contain_count += 1

        # if a starts before b then it needs to end after B starts
        if rangeA[0] <= rangeB[0] <= rangeA[1]:
            any_overlap_count += 1
        # if a starts after b then b must end after a starts
        elif rangeB[0] <= rangeA[0] <= rangeB[1]:
            any_overlap_count += 1
    print(f'Number of pairs totally contained {total_contain_count}')
    print(f'Number of pairs with any overlap  {any_overlap_count}')
