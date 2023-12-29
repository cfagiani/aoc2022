import sys
from collections import deque


class Valve:
    def __init__(self, input):
        # Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
        # Valve XX has flow rate=0; tunnels lead to valve YY

        tokens = input.split(' ')
        self.name = tokens[1]
        self.rate = int(tokens[4].split('=')[1].replace(';', ''))
        self.open = False
        if 'to valves' in input:
            self.paths = input.split(' to valves ')[1].split(', ')
        else:
            self.paths = [input.split(' to valve ')[1]]

    def get_name(self):
        return self.name

    def get_paths(self):
        return self.paths

    def is_open(self):
        return self.open

    def open_valve(self):
        self.open = True

    def get_rate(self):
        return self.rate

    def get_potential_flow(self, time_remaining):
        return self.rate * time_remaining


def get_flow(valves):
    total = 0
    for valve in valves.values():
        if valve.is_open():
            total += valve.get_rate()
    return total


def get_shortest_path(start, valves):
    distances = {start: 0}
    visited = {}
    paths = {}
    while len(visited) < len(valves):
        un_visisted = {k: v for k, v in distances.items() if visited.get(k) is None}
        cur_node = min(un_visisted, key=lambda x: x[1])
        for path in valves[cur_node].get_paths():
            old_dist = distances.get(path, sys.maxsize)
            if distances.get(cur_node) + 1 < old_dist:
                distances[path] = distances.get(cur_node) + 1
                old_path = paths.get(cur_node, []).copy()
                old_path.append(path)
                paths[path] = old_path
        visited[cur_node] = True
    return paths


def get_next_move(valves, cur_loc, time_remaining):
    # find the number of steps needed to reach each open valve
    shortest_paths = get_shortest_path(cur_loc, valves)
    max_potential_flow = 0
    max_potential_flow_path = None
    for path in shortest_paths.items():
        if not valves.get(path[0]).is_open():
            potential_flow = ((time_remaining - len(path[1]))-1) * valves.get(path[0]).get_rate()
            if potential_flow > max_potential_flow:
                max_potential_flow_path = path
                max_potential_flow = potential_flow

    return max_potential_flow_path


valves = {}
with open('../input/day16.txt', 'rt') as infile:
    for line in infile.readlines():
        valve = Valve(line.strip())
        valves[valve.get_name()] = valve

max_time = 30
cur_time = 1
pressure_released = 0
cur_loc = 'AA'
next_path = None
while cur_time < max_time:
    opened_valve = False
    pressure_released += get_flow(valves)
    if next_path is not None and next_path[0] == cur_loc:
        valves.get(cur_loc).open_valve()
        print(f'Minute {cur_time}\nOpened {cur_loc}')
        opened_valve = True
        next_path = None
    if next_path is None:
        next_path = get_next_move(valves, cur_loc, max_time - cur_time)

    if not opened_valve and next_path is not None:
        # only move if we didn't open a valve
        cur_loc = next_path[1].pop(0)
        print(f'Minute {cur_time}\nMoved to {cur_loc}')
    cur_time += 1


print(f'Released {pressure_released}')
