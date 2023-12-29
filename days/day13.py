class PacketPair:
    def __init__(self, first, second):
        self.left = eval(first.strip())
        self.right = eval(second.strip())

    def is_valid(self):
        return is_in_order(self.left, self.right)


def is_in_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    if isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            if i > len(right) - 1:
                return False
            valid = is_in_order(left[i], right[i])
            if valid is not None:
                return valid
        return True
    else:
        if isinstance(left, int):
            return is_in_order([left], right)
        else:
            return is_in_order(left, [right])


def insert_packet(packet, all_packets):
    if len(all_packets) == 0:
        all_packets.append(packet)
    else:
        for idx in range(len(all_packets)):
            if is_in_order(packet, all_packets[idx]):
                all_packets.insert(idx, packet)
                return
        all_packets.append(packet)


def find_idx(search, all_packets):
    for idx, packet in enumerate(all_packets):
        if packet == search:
            return idx + 1
    return -1


with open('../input/day13.txt', 'rt') as infile:
    lines = infile.readlines()
    packet_pairs = []

    for i in range(0, len(lines), 3):
        packet_pairs.append(PacketPair(lines[i], lines[i + 1]))

    correct_order_sum = 0
    for i, packet in enumerate(packet_pairs):
        if packet.is_valid():
            correct_order_sum += (i + 1)
    print(f'Sum of indices of packets in correct order: {correct_order_sum}')
    all_packets = []
    for pair in packet_pairs:
        insert_packet(pair.left, all_packets)
        insert_packet(pair.right, all_packets)

    insert_packet([[2]], all_packets)
    insert_packet([[6]], all_packets)

    print(f'Decode key {find_idx([[6]], all_packets) * find_idx([[2]], all_packets)}')
