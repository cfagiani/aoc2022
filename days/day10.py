clock = 1
register = 1
interesting_cycles = [20, 60, 100, 140, 180, 220]
signal_strengths = 0
screen = [[''] * 40 for x in range(6)]


def render(cycle, sprite, buffer):
    if abs((cycle - 1) % 40 - sprite) <= 1:
        buffer[int(cycle / 40)][(cycle - 1) % 40] = '#'
    elif int(cycle / 40) < len(buffer):
        buffer[int(cycle / 40)][(cycle - 1) % 40] = '.'


with open('../input/day10.txt', 'rt') as infile:
    for line in infile.readlines():
        instruction = line.strip()
        if clock in interesting_cycles:
            signal_strengths += register * clock
        render(clock, register, screen)
        if instruction == 'noop':
            clock += 1
        else:
            args = instruction.split(' ')
            clock += 1
            if clock in interesting_cycles:
                signal_strengths += register * clock
            render(clock, register, screen)
            clock += 1
            register += int(args[1])
print(f'Total signal strength: {signal_strengths}')
for line in screen:
    print(''.join(line))
