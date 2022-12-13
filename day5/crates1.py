import sys,os

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        return file_content.readlines()

def follow_instructions(move):
    return #crate_stack_change

for line in (read_file("cratesparsetest.txt")):
    if line.startswith("move"):
        placeholder = 0 # follow instructions
    else:
        placeholder = 0 # parse crate start position