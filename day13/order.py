import sys
import os
import ast
import itertools


def main():
    packets = parse_file("sample.txt")
    left_and_right_packets = split_packets(packets)
    left_packets, right_packets = left_and_right_packets[0], left_and_right_packets[1]
    number_of_pairs = get_number_of_pairs(left_packets, right_packets)

    sum_of_correct_indices = 0
    iterations = range(number_of_pairs)
    for i in iterations:
        correct_order = compare_packets(left_packets[i], right_packets[i])
        if correct_order:
            print(i + 1)
            sum_of_correct_indices += i + 1
    
    print("Total: " + str(sum_of_correct_indices))


def compare_packets(left, right):
    for left_value, right_value in itertools.zip_longest(left, right, fillvalue=None):

        if left_value == None:
            return True
        if right_value == None:
            return False

        value_type = compare_type(left_value, right_value)
        
        if value_type == 'int':
            if left_value < right_value:
                return True
            if left_value > right_value:
                return False
        else:
            left_value, right_value = type_correction(left_value, right_value)
            deeper_compare = compare_packets(left_value, right_value)

            if deeper_compare == True or deeper_compare == False:
                return deeper_compare


def compare_type(left_value, right_value):
    if type(left_value) is int and type(right_value) is int:
        return 'int'
    else: 
        return 'not_int'


def type_correction(left_value, right_value):
    if (type(left_value) is int):
        left_value = [left_value]
    if (type(right_value) is int):
        right_value = [right_value]
    return left_value, right_value
        

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


def get_number_of_pairs(first, second):
    if len(first) != len(second):
        raise Exception("var1 and var2 do not contain the same number of packets")
    else:
        return len(first)


if __name__ == "__main__":
    main()