import sys,os

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        return file_content.readlines()

for line in (read_file("input.txt")):
    elf_pair = (str(line).strip())
    