import sys
import os
import math
import collections
import re

def main():
    content = read_file("input.txt")
    print(*content, sep='\n')
    print(content)
    monkey_data = build_monkey_dict(content)
    print(monkey_data)

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        return file_content.read().split('\n')

def build_monkey_dict(input):
    monkey_dict = collections.OrderedDict()
    for line in input:
        if 'Monkey' in line:
            monkey_number = re.findall('\d', line)
            monkey_dict['Monkey' + str(monkey_number[0])] = {}
        elif 'Starting items' in line:
            held_items = re.findall('\d+', line)
            monkey_dict['Monkey' + str(monkey_number[0])]['items'] = held_items
        elif 'Operation' in line:
            operation = (re.search('old (\+|\-\/|\*)', line)).group(1)
            number = re.findall('\d+', line)
            if number:
                monkey_dict['Monkey' + str(monkey_number[0])]['Operation'] = str(operation) + str(number[0])
            else:
                monkey_dict['Monkey' + str(monkey_number[0])]['Operation'] = str(operation) + str(operation)
        elif 'Test' in line:
            number = re.findall('\d+', line)
            monkey_dict['Monkey' + str(monkey_number[0])]['DivideByTestNumber'] = int(number[0])  
        elif 'true' in line:
            number = re.findall('\d+', line)
            monkey_dict['Monkey' + str(monkey_number[0])]['TrueThrowTarget'] = 'Monkey' + str(number[0])
        elif 'false' in line:
            number = re.findall('\d+', line)
            monkey_dict['Monkey' + str(monkey_number[0])]['FalseThrowTarget'] = 'Monkey' + str(number[0])
    return monkey_dict

def test_worry_level(current_worry_level):
    return math.floor((current_worry_level * 19) / 3)

def choose_monkey_target(current_worry_level, test_number):
    if test_worry_level(current_worry_level) % test_number == 0:
        return # monkey number if true
    else:
        return # monkey number if false

def choose_monkey():
    return

def throw_item():
    return

if __name__ == "__main__":
    main()