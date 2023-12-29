def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


class Sensor:
    def __init__(self, pos, dist):
        self.position = pos
        self.nearest_beacon_dist = dist

    def is_closer_than_beacon(self, pos):
        dist = manhattan_dist(self.position, pos)
        return dist < self.nearest_beacon_dist

    def get_covered_positions(self, y_pos):
        # early escape if the y_pos is farther away than the beacon
        x_range = self.nearest_beacon_dist - abs(self.position[1] - y_pos)
        if x_range < 0 or x_range > self.nearest_beacon_dist:
            return None

        return tuple(sorted((self.position[0] - x_range, self.position[0] + x_range)))


def extract_point(input_string):
    parts = input_string.split('=')
    return (int(parts[1].split(',')[0]), int(parts[2]))


def calc_ranges(sensors, y_pos):
    ranges = []
    for sensor in sensors:
        sensor_range = sensor.get_covered_positions(y_pos)
        if sensor_range is not None:
            ranges.append(sensor_range)
    ranges.sort(key=lambda x: x[0])
    merged_ranges = [ranges.pop(0)]
    for sensor_range in ranges:
        if merged_ranges[0][0] <= sensor_range[0] <= merged_ranges[0][1]:
            # start of sensor range is somewhere inside the top of the stack
            if sensor_range[1] > merged_ranges[0][1]:
                # if sensor_range extends beyond the end of the top of the stack, extend it
                merged_ranges[0] = (merged_ranges[0][0], sensor_range[1])
        else:
            merged_ranges.insert(0, sensor_range)

    return merged_ranges


def find_distress(sensors):
    max_val = 4000000
    for y in range(max_val):
        row_ranges = calc_ranges(sensors, y)
        if len(row_ranges) > 1:
            row_ranges.sort(key=lambda x: x[0])
            for r in row_ranges:
                if r[0] > 1 and r[0] < max_val:
                    return (r[0] - 1, y)
                if r[0] > 0 and r[0] < max_val:
                    return (r[1] + 1, y)
    return None


with open('../input/day15.txt', 'rt') as infile:
    sensors = []
    beacons = []
    for line in infile.readlines():
        line_parts = line.strip().split(': closest beacon is at ')
        sensor_pos = extract_point(line_parts[0])
        beacon_pos = extract_point(line_parts[1])
        beacons.append(beacon_pos)
        dist = manhattan_dist(sensor_pos, beacon_pos)

        sensors.append(Sensor(sensor_pos, dist))

row_ranges = calc_ranges(sensors, 2000000)
total_pos = 0
for r in row_ranges:
    total_pos += r[1] - r[0]

print(f'Positions that cannot have a beacon {total_pos}')

distress_coords = find_distress(sensors)
print(f'Tuning frequency: {(distress_coords[0] * 4000000) + distress_coords[1]}')
