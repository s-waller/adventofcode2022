import sys,os,re,json

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

def get_file_size(input):
    return input.split()[0]

def change_depth(argument):
    if argument == "..":
        return - 1
    elif argument == "/":
        return 0
    else:
        return 1

def find_totals(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find_totals(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find_totals(key, d):
                    yield result

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
depth = -1

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
                current_directory = argument
                if not tree_size.get(current_directory):
                    tree_size[current_directory] = {}
                if not tree_size.get(current_directory,{}).get("total"):
                    tree_size[current_directory]["total"] = 0

            else:
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

                depth = depth + change_depth_result
            
        elif command_type == "ls":
            continue

    elif line_type == "sub_directory":
        directory_name = get_argument(stripped_line)
        if int(depth) == 0:
            if not tree_size.get(current_directory,{}).get(directory_name):
                tree_size[current_directory][directory_name] = {}
                tree_size[current_directory][directory_name]["total"] = 0
        elif depth == 1:
            if not tree_size.get(previous_directory_1,{}).get(current_directory,{}).get(directory_name):
                tree_size[previous_directory_1][current_directory][directory_name] = {}
                tree_size[previous_directory_1][current_directory][directory_name]["total"] = 0
        elif depth == 2:
            if not tree_size.get(previous_directory_2,{}).get(previous_directory_1,{}).get(current_directory,{}).get(directory_name):
                tree_size[previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
                tree_size[previous_directory_2][previous_directory_1][current_directory][directory_name]["total"] = 0
        elif depth == 3:
            if not tree_size.get(previous_directory_3,{}).get(previous_directory_2,{}).get(previous_directory_1,{}).get(current_directory,{}).get(directory_name):
                tree_size[previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
                tree_size[previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]["total"] = 0
        elif depth == 4:
            if not tree_size.get(previous_directory_4,{}).get(previous_directory_3,{}).get(previous_directory_2,{}).get(previous_directory_1,{}).get(current_directory,{}).get(directory_name):
                tree_size[previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
                tree_size[previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]["total"] = 0
        elif depth == 5:
            if not tree_size.get(previous_directory_5,{}).get(previous_directory_4,{}).get(previous_directory_3,{}).get(previous_directory_2,{}).get(previous_directory_1,{}).get(current_directory,{}).get(directory_name):
                tree_size[previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
                tree_size[previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]["total"] = 0
        elif depth == 6:
            if not tree_size.get(previous_directory_6,{}).get(previous_directory_5,{}).get(previous_directory_4,{}).get(previous_directory_3,{}).get(previous_directory_2,{}).get(previous_directory_1,{}).get(current_directory,{}).get(directory_name):
                tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
                tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]["total"] = 0
        elif depth == 7:
            if not tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]:
                tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
                tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]["total"] = 0
        elif depth == 8:
            if not tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]:
                tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name] = {}
                tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][directory_name]["total"] = 0
        

    elif line_type == "file":
        file_size = get_file_size(stripped_line)

        file_name = get_argument(stripped_line)
        if int(depth) == 0:
            if not tree_size.get(current_directory,{}).get(file_name):
                tree_size[current_directory][file_name] = file_size
                tree_size[current_directory]["total"] = tree_size[current_directory]["total"] + int(file_size)
        elif depth == 1:
            if not tree_size.get(previous_directory_1,{}).get(current_directory,{}).get(file_name):
                tree_size[previous_directory_1][current_directory][file_name] = file_size
                tree_size[previous_directory_1][current_directory]["total"] = tree_size[previous_directory_1][current_directory]["total"] + int(file_size)
                tree_size[previous_directory_1]["total"] = tree_size[previous_directory_1]["total"] + int(file_size)
        elif depth == 2:
            if not tree_size.get(previous_directory_2,{}).get(previous_directory_1,{}).get(current_directory,{}).get(file_name):
                tree_size[previous_directory_2][previous_directory_1][current_directory][file_name] = file_size
                tree_size[previous_directory_2][previous_directory_1][current_directory]["total"] = tree_size[previous_directory_2][previous_directory_1][current_directory]["total"] + int(file_size)
                tree_size[previous_directory_2][previous_directory_1]["total"] = tree_size[previous_directory_2][previous_directory_1]["total"] + int(file_size)
                tree_size[previous_directory_2]["total"] = tree_size[previous_directory_2]["total"] + int(file_size)
        elif depth == 3:
            if not tree_size.get(previous_directory_3,{}).get(previous_directory_2,{}).get(previous_directory_1,{}).get(current_directory,{}).get(file_name):
                tree_size[previous_directory_3][previous_directory_2][previous_directory_1][current_directory][file_name] = file_size
                tree_size[previous_directory_3][previous_directory_2][previous_directory_1][current_directory]["total"] = tree_size[previous_directory_3][previous_directory_2][previous_directory_1][current_directory]["total"] + int(file_size)
                tree_size[previous_directory_3][previous_directory_2][previous_directory_1]["total"] = tree_size[previous_directory_3][previous_directory_2][previous_directory_1]["total"] + int(file_size)
                tree_size[previous_directory_3][previous_directory_2]["total"] = tree_size[previous_directory_3][previous_directory_2]["total"] + int(file_size)
                tree_size[previous_directory_3]["total"] = tree_size[previous_directory_3]["total"] + int(file_size)
        elif depth == 4:
            if not tree_size.get(previous_directory_4,{}).get(previous_directory_3,{}).get(previous_directory_2,{}).get(previous_directory_1,{}).get(current_directory,{}).get(file_name):
                tree_size[previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][file_name] = file_size
                tree_size[previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory]["total"] = tree_size[previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory]["total"] + int(file_size)
                tree_size[previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1]["total"] = tree_size[previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1]["total"] + int(file_size)
                tree_size[previous_directory_4][previous_directory_3][previous_directory_2]["total"] = tree_size[previous_directory_4][previous_directory_3][previous_directory_2]["total"] + int(file_size)
                tree_size[previous_directory_4][previous_directory_3]["total"] = tree_size[previous_directory_4][previous_directory_3]["total"] + int(file_size)
                tree_size[previous_directory_4]["total"] = tree_size[previous_directory_4]["total"] + int(file_size)
        elif depth == 5:
            if not tree_size.get(previous_directory_5,{}).get(previous_directory_4,{}).get(previous_directory_3,{}).get(previous_directory_2,{}).get(previous_directory_1,{}).get(current_directory,{}).get(file_name):
                tree_size[previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][file_name] = file_size
                tree_size[previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory]["total"] = tree_size[previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory]["total"] + int(file_size)
                tree_size[previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1]["total"] = tree_size[previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1]["total"] + int(file_size)
                tree_size[previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2]["total"] = tree_size[previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2]["total"] + int(file_size)
                tree_size[previous_directory_5][previous_directory_4][previous_directory_3]["total"] = tree_size[previous_directory_5][previous_directory_4][previous_directory_3]["total"] + int(file_size)
                tree_size[previous_directory_5][previous_directory_4]["total"] = tree_size[previous_directory_5][previous_directory_4]["total"] + int(file_size)
                tree_size[previous_directory_5]["total"] = tree_size[previous_directory_5]["total"] + int(file_size)
        elif depth == 6:
            if not tree_size.get(previous_directory_6,{}).get(previous_directory_5,{}).get(previous_directory_4,{}).get(previous_directory_3,{}).get(previous_directory_2,{}).get(previous_directory_1,{}).get(current_directory,{}).get(file_name):
                tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][file_name] = file_size
                tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory]["total"] = tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory]["total"] + int(file_size)
                tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1]["total"] = tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1]["total"] + int(file_size)
                tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2]["total"] = tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2]["total"] + int(file_size)
                tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3]["total"] = tree_size[previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3]["total"] + int(file_size)
                tree_size[previous_directory_6][previous_directory_5][previous_directory_4]["total"] = tree_size[previous_directory_6][previous_directory_5][previous_directory_4]["total"] + int(file_size)
                tree_size[previous_directory_6][previous_directory_5]["total"] = tree_size[previous_directory_6][previous_directory_5]["total"] + int(file_size)
                tree_size[previous_directory_6]["total"] = tree_size[previous_directory_6]["total"] + int(file_size)
        elif depth == 7:
            if not tree_size.get(previous_directory_7,{}).get(previous_directory_6,{}).get(previous_directory_5,{}).get(previous_directory_4,{}).get(previous_directory_3,{}).get(previous_directory_2,{}).get(previous_directory_1,{}).get(current_directory,{}).get(file_name):
                tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][file_name] = file_size
                tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory]["total"] = tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory]["total"] + int(file_size)
                tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1]["total"] = tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1]["total"] + int(file_size)
                tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2]["total"] = tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2]["total"] + int(file_size)
                tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3]["total"] = tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3]["total"] + int(file_size)
                tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4]["total"] = tree_size[previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4]["total"] + int(file_size)
                tree_size[previous_directory_7][previous_directory_6][previous_directory_5]["total"] = tree_size[previous_directory_7][previous_directory_6][previous_directory_5]["total"] + int(file_size)
                tree_size[previous_directory_7][previous_directory_6]["total"] = tree_size[previous_directory_7][previous_directory_6]["total"] + int(file_size)
                tree_size[previous_directory_7]["total"] = tree_size[previous_directory_7]["total"] + int(file_size)
        elif depth == 8:
            if not tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][file_name]:
                tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory][file_name] = file_size
                tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory]["total"] = tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1][current_directory]["total"] + int(file_size)
                tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1]["total"] = tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2][previous_directory_1]["total"] + int(file_size)
                tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2]["total"] = tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3][previous_directory_2]["total"] + int(file_size)
                tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3]["total"] = tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4][previous_directory_3]["total"] + int(file_size)
                tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4]["total"] = tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5][previous_directory_4]["total"] + int(file_size)
                tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5]["total"] = tree_size[previous_directory_8][previous_directory_7][previous_directory_6][previous_directory_5]["total"] + int(file_size)
                tree_size[previous_directory_8][previous_directory_7][previous_directory_6]["total"] = tree_size[previous_directory_8][previous_directory_7][previous_directory_6]["total"] + int(file_size)
                tree_size[previous_directory_8][previous_directory_7]["total"] = tree_size[previous_directory_8][previous_directory_7]["total"] + int(file_size)
                tree_size[previous_directory_8]["total"] = tree_size[previous_directory_8]["total"] + int(file_size)


print (json.dumps(tree_size, indent=4, default=str))

list_of_totals = list(find_totals("total", tree_size))

end_total = 0
for i in list_of_totals:
    if i > 100000:
        continue
    else:
        end_total = end_total + int(i)

print(end_total)