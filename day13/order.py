import sys
import os
import ast

def main():
    packets = parse_file("sample.txt")
    left_and_right_packets = split_packets(packets)
    left_packets, right_packets = left_and_right_packets[0], left_and_right_packets[1]



def parse_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        lines = file_content.read().split('\n')

    lines = [line for i, line in enumerate(lines) if line != '']

    for i, line in enumerate(lines):
        lines[i] = ast.literal_eval(line)
    return lines

def split_packets(list_of_packets):
    left_list = list_of_packets[::2]
    right_list = list_of_packets[1::2]
    return left_list, right_list

if __name__ == "__main__":
    main()