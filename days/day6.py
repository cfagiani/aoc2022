def contains_dupe(code):
    code_set = set(list(code))
    return len(code_set) != len(code)


def find_marker(marker_len):
    with open('../input/day6.txt', 'rt') as infile:
        datastream = infile.read()
        for i in range(0, len(datastream) - marker_len):
            if not contains_dupe(datastream[i:i + marker_len]):
                print(f'Code found after char {i + marker_len}')
                break


print('Start of packet')
find_marker(4)
print('Start of message')
find_marker(14)
