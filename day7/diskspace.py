import sys,os,re

def read_lines(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        return file_content.readlines()

def line_parse(input):
    if (input)[0] == "$":
        return "shell_command"
    elif (input).split()[0] == "dir":
        return "sub_directory"
    elif bool(re.search(r'\d', (input).split()[0])):
        return "file"
    else:
        return

def parse_command(input):
    return input.split()[1]

def get_argument(input):
    return input.split()[-1]

def change_depth(argument):
    if argument == "..":
        return - 1
    elif argument == "/":
        return 0
    else:
        return 1


def run_command(command):
    
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

##########################################################

for line in read_lines("input.txt"):
    stripped_line = line.strip()
    line_type = line_parse(stripped_line)

    if line_type == "shell_command":
        command_type = parse_command(stripped_line)

        if command_type == "cd":
            argument = get_argument(stripped_line)
            change_depth_result = change_depth(argument)

            if change_depth_result == 0:
                depth = 0
            else:
                depth = depth + change_depth_result
                if change_depth_result > 0:
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
                    line_type == "sub_directory"

                if change_depth_result < 0:
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
            
        elif command_type == "ls":
            print(tree_size)

    elif line_type == "sub_directory":
        directory_name = get_argument(stripped_line)
        if int(depth) == 0:
            if not tree_size[current_directory][directory_name]:
                tree_size[current_directory][directory_name] = {}
        elif depth == 1:
            if not tree_size[previous_directory_1][current_directory][directory_name]:
                tree_size[previous_directory_1][current_directory][directory_name] = {}
        elif depth == 2:
            if not tree_size[previous_directory_2][previous_directory_1][current_directory][directory_name]:
                tree_size[previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
        elif depth == 3:
            if not tree_size[previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]:
                tree_size[previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
        elif depth == 4:
            if not tree_size[previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]:
                tree_size[previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
        elif depth == 5:
            if not tree_size[previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]:
                tree_size[previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
        elif depth == 6:
            if not tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]:
                tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
        elif depth == 7:
            if not tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]:
                tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
        elif depth == 8:
            if not tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]:
                tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
        elif depth == 9:
            if not tree_size[previous_directory_9][previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]:
                tree_size[previous_directory_9][previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name] = {}



    elif line_type == "file":


result = list(getpaths(tree_size))
print(result)
print(tree_size)
