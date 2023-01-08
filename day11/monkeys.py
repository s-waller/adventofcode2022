import sys
import os
import math
import collections
import re

def main():
    content = read_file("input.txt")
    print(*content, sep='\n')
    print(content)
    build_monkey_dict(content)

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        return file_content.read().split('\n')

# def build_monkey_dict Monkey 0:
def build_monkey_dict(input):
    monkey_dict = collections.OrderedDict()
    monkey_index = 0
    starting_items_index = 0
    operation_index = 0
    test_index = 0
    if_true_index = 0
    if_false_index = 0

    for line in input:
        if 'Monkey' in line:
            monkey_number = re.findall('\d', line)
            print('Monkey' + str(monkey_number[0]))
            monkey_index += 1
        elif 'Starting items' in line:
            held_items = re.findall('\d+', line)
            print('Starting items = ' + str(held_items))
            starting_items_index += 1
        elif 'Operation' in line:
            operation = (re.search('old (\+|\-\/|\*)', line)).group(1)
            number = re.findall('\d+', line)
            if number:
                print('Operation = ' + str(operation) + ' ' + str(number[0]))
            else:
                print('Operation = ' + str(operation) + ' ' + str(operation))
            operation_index += 1
        elif 'Test' in line:
            number = re.findall('\d+', line)
            print('Divide by ' + str(number[0]))    
            test_index += 1
        elif 'true' in line:
            number = re.findall('\d+', line)
            print('True so throw to Monkey' + str(number[0]))
            if_true_index += 1
        elif 'false' in line:
            number = re.findall('\d+', line)
            print('False so throw to Monkey' + str(number[0]))  
            if_false_index += 1

# def assign_starting_numbers Starting items: 79, 98



def worry_level(current_worry_level):
    return math.floor((current_worry_level * 19) / 3)

def asses_worry_level(current_worry_level, test_number):
    if worry_level(current_worry_level) % test_number == 0:
        return # monkey number if true
    else:
        return # monkey number if false

def choose_monkey():
    return

if __name__ == "__main__":
    main()