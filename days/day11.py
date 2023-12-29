class Monkey:
    def __init__(self, config):
        lines = config.split('\n')
        self.name = int(lines[0].strip().replace(':', ''))
        self.items = [int(worry) for worry in lines[1].strip().replace('Starting items: ', '').split(',')]
        self.operation = lines[2].strip().split(' = ')[1]
        self.divisor = int(lines[3].strip().split('divisible by ')[1])
        self.true_dest = int(lines[4].strip().split('throw to monkey ')[1])
        self.false_dest = int(lines[5].strip().split('throw to monkey ')[1])
        self.inspection_count = 0

    def get_name(self):
        return self.name

    def take_turn(self, divide_worry=True, divisor_product=None):
        """
        return list of throws. throws are tuples with first entry being destination monkey and second being worry level
        :return:
        """
        throws = []
        while len(self.items) > 0:
            self.inspection_count += 1
            item = self.items.pop(0)
            worry_level = eval(self.operation, {'old': item})
            if divide_worry:
                worry_level = int(worry_level / 3)
            if divisor_product is not None:
                worry_level = worry_level % divisor_product
            if worry_level % self.divisor == 0:
                throws.append((self.true_dest, worry_level))
            else:
                throws.append((self.false_dest, worry_level))
        return throws

    def catch(self, item):
        self.items.append(item)

    def get_inspection_count(self):
        return self.inspection_count

    def get_divisor(self):
        return self.divisor


def initialize_monkeys():
    with open('../input/day11.txt', 'rt') as infile:
        contents = infile.read()

    config = contents.split('Monkey ')
    monkeys = {}
    for monkey_conf in config:
        if len(monkey_conf.strip()) > 0:
            monkey = Monkey(monkey_conf)
            monkeys[monkey.get_name()] = monkey
    return monkeys


def run_game(turns, divide_worry):
    monkeys = initialize_monkeys()
    divisor_product = 1
    for monkey in monkeys.values():
        divisor_product *= monkey.get_divisor()
    for i in range(turns):
        for j in range(len(monkeys)):
            monkey = monkeys.get(j)
            throws = monkey.take_turn(divide_worry, divisor_product if divide_worry is False else None)
            for throw in throws:
                monkeys.get(throw[0]).catch(throw[1])
    busy_list = sorted(list(monkeys.values()), key=lambda m: m.get_inspection_count(), reverse=True)
    print(f'Monkey business level: {busy_list[0].get_inspection_count() * busy_list[1].get_inspection_count()}')


print('Part 1')
run_game(20, True)
print('Part 2')
run_game(10000, False)
