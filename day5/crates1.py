import sys,os,re

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        return file_content.readlines()

def get_starting_positions(crate_info):
    return re.findall('....?',crate_info)

def create_lists(starting_position_line):
    return # placeholder

def follow_instructions(move):
    return # crate_stack_change

for line in (read_file("cratesparsetest.txt")):
    if line.startswith("move"):
        placeholder = 0 # follow instructions
    else:
        print(get_starting_positions(line)) # parse crate start position