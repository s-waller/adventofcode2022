import sys
import os
import ast

def main():
    packets = parse_file("sample.txt")
    left_and_right_packets = split_packets(packets)
    left_packets, right_packets = left_and_right_packets[0], left_and_right_packets[1]


# If both values are integers, the lower integer should come first
# If the left integer is lower than the right integer, the inputs are in the right order
# If the left integer is higher than the right integer, the inputs are not in the right order
# Otherwise, the inputs are the same integer; continue checking the next part of the input

# If both values are lists, compare the first value of each list, then the second value, and so on
# If the left list runs out of items first, the inputs are in the right order
# If the right list runs out of items first, the inputs are not in the right order
# If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input

# If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison
# For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2]




# What are the indices of the pairs that are already in the right order? 
# (The first pair has index 1, the second pair has index 2, and so on.) 
# In the above example, the pairs in the right order are 1, 2, 4, and 6; the sum of these indices is 13.

# Determine which pairs of packets are already in the right order
# What is the sum of the indices of those pairs?


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