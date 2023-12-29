class FSEntry:

    def __init__(self, type, name, size):
        self.type = type
        self.size = size
        self.name = name
        self.parent = None
        self.entries = {}

    def add_item(self, entry):
        entry.set_parent(self)
        self.entries[entry.get_name()] = entry

    def get_size(self):
        if self.type == 'F':
            return self.size
        else:
            return self.__get_child_size()

    def __get_child_size(self):
        total = 0
        for entry in self.entries.values():
            total += entry.get_size()
        return total

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def set_parent(self, parent):
        self.parent = parent

    def subdirs(self):
        return [v for v in self.entries.values() if v.get_type() == 'D']

    def cwd(self, dir_name):
        if '..' == dir_name.strip():
            return self.parent
        else:
            return self.entries.get(dir_name.strip(), None)


def get_dir_sizes(cur_dir, parent_path, dir_map):
    for subdir in cur_dir.subdirs():
        get_dir_sizes(subdir, f'{parent_path}{cur_dir.get_name()}/', dir_map)
    dir_map[f'{parent_path}{cur_dir.get_name()}'] = cur_dir.get_size()


fs_root = FSEntry('D', '', 0)
cur_dir = fs_root
with open('../input/day7.txt', 'rt') as infile:
    idx = 0
    lines = infile.readlines()
    while idx < len(lines):
        if lines[idx].strip().startswith('$ cd'):
            dest_dir = lines[idx].strip()[len('$ cd'):].strip()
            if dest_dir == '/':
                cur_dir = fs_root
            else:
                cur_dir = cur_dir.cwd(dest_dir)
            idx += 1
        elif lines[idx].strip().startswith('$ ls'):
            idx += 1
            while idx < len(lines) and not lines[idx].startswith('$'):
                parts = lines[idx].split(' ')
                if parts[0] == 'dir':
                    cur_dir.add_item(FSEntry('D', parts[1].strip(), 0))
                else:
                    cur_dir.add_item(FSEntry('F', parts[1].strip(), int(parts[0].strip())))
                idx += 1
    dir_map = {}
    get_dir_sizes(fs_root, '', dir_map)
    filtered_dir = {k: v for (k, v) in dir_map.items() if v <= 100000}
    total_filtered_size = 0
    for dir_size in filtered_dir.values():
        total_filtered_size += dir_size
    print(f'filtered Total size (part1): {total_filtered_size}')

    free_space = 70000000 - fs_root.get_size()
    space_needed = 30000000 - free_space
    print(f'Starting free space {free_space}. Need additional {space_needed}')
    candidates_to_delete = [v for (k, v) in dir_map.items() if v >= space_needed]
    candidates_to_delete.sort()
    print(f'Size of smallest dir to delete to make enough space (part2): {candidates_to_delete[0]}')
