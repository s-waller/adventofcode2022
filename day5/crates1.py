import sys,os,re

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        return file_content.readlines()

def get_starting_positions(crate_info):
    return re.findall('....?',crate_info)

def create_lists(starting_position_line):
    list = []
    for i in starting_position_line:
        list += i[1]
    return list

def contains_numbers(line_input):
    return bool(re.search(r'\d', line_input))

def follow_instructions(move):
    return # crate_stack_change

for line in (read_file("cratesparsetest.txt")):
    if line == '\n':
        continue
    if line.startswith("move"):
        placeholder = 0 # follow instructions
    elif contains_numbers(line):
        print("line contains numbers")
    else:
        starting_positions = (get_starting_positions(line))
        print(create_lists(starting_positions))