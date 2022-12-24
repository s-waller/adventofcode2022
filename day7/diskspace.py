import sys,os

def read_lines(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        return file_content.readlines()

def command_parse(input):
    return

def change_depth(command):


def run_command(command):
    if len(command) > 1:
        argument = command[1]
        command_base = command[0]
        if command_base == "cd":
            if argument == "..":
                current_directory = previous_directory_1
                previous_directory_1 = previous_directory_2
                previous_directory_2 = previous_directory_3
                previous_directory_3 = previous_directory_4
                previous_directory_4 = previous_directory_5
                previous_directory_5 = previous_directory_6
                previous_directory_6 = previous_directory_7
                previous_directory_7 = previous_directory_8
                previous_directory_8 = previous_directory_9
                previous_directory_9 = None
                depth = depth - 1
            elif argument == "/":
                tree_size[argument] = {}
                current_directory = argument
                depth = 0
            else:
                tree_size[current_directory][argument] = {}
                previous_directory_9 = previous_directory_8
                previous_directory_8 = previous_directory_7
                previous_directory_7 = previous_directory_6
                previous_directory_6 = previous_directory_5
                previous_directory_5 = previous_directory_4
                previous_directory_4 = previous_directory_3
                previous_directory_3 = previous_directory_2
                previous_directory_2 = previous_directory_1
                previous_directory_1 = current_directory
                current_directory = argument
                depth = depth + 1
        else:
            return

def getpaths(d):
    if not isinstance(d, dict):
        yield [d]
    else:
        yield from ([k] + w for k, v in d.items() for w in getpaths(v))

previous_directory_9 = None
previous_directory_8 = None
previous_directory_7 = None
previous_directory_6 = None
previous_directory_5 = None
previous_directory_4 = None
previous_directory_3 = None
previous_directory_2 = None
previous_directory_1 = None
current_directory = None
tree_size = {}
depth = 0

for line in read_lines("input.txt"):
    stripped_line = line.strip().split()
    if (stripped_line)[0] == "$":
        command = stripped_line[1:]
        run_command(command)
        print(command)
    elif str(stripped_line)[0] == "dir":
        if int(depth) == 0:
            tree_size[current_directory][str(stripped_line[1])] = {}
        elif depth == 1:
            tree_size[previous_directory_1][current_directory][str(stripped_line[1])] = {}
        elif depth == 2:
            tree_size[previous_directory_2][previous_directory_1][current_directory][str(stripped_line[1])] = {}
        elif depth == 3:
            tree_size[previous_directory_3][previous_directory_2][previous_directory_1][current_directory][str(stripped_line[1])] = {}
        elif depth == 4:
            tree_size[previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][str(stripped_line[1])] = {}
        elif depth == 5:
            tree_size[previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][str(stripped_line[1])] = {}
        elif depth == 6:
            tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][str(stripped_line[1])] = {}
        elif depth == 7:
            tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][str(stripped_line[1])] = {}
        elif depth == 8:
            tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][str(stripped_line[1])] = {}
        elif depth == 9:
            tree_size[previous_directory_9][previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][str(stripped_line[1])] = {}


result = list(getpaths(tree_size))
print(result)
print(tree_size)
