import sys
import os
import math
import collections
import re
from pprint import pprint
import operator
import time

def main():
    content = read_file("input.txt")
    monkey_data = build_monkey_dict(content)
    pprint(monkey_data, sort_dicts=False)

    for i in range(20): # 20 rounds
        for monkey in monkey_data:
            single_monkey = monkey_data.get(monkey)
            while single_monkey['items']:
                current_item = int(single_monkey['items'][0])
                new_item_value = int(inspect_item(single_monkey, current_item))
                target = choose_monkey_target(single_monkey, new_item_value)
                target_monkey_info = monkey_data.get(target)
                throw_item(single_monkey, target_monkey_info, new_item_value)
                time.sleep(0.0005)
                print("\033c")
                print(monkey)
                pprint(monkey_data[monkey], sort_dicts=False)

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

def inspect_item(monkey_info, item):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "**": operator.pow
    }   
    selected_operator = ''.join(re.findall('[^\d]', monkey_info['Operation']))
    try:
        number = int(re.findall('\d+', monkey_info['Operation'])[0])
    except:
        number = 2
    worry_increase = operators[selected_operator](item, number)
    result = math.floor(worry_increase / 3)
    monkey_info['items'][0] = result
    return result

def choose_monkey_target(monkey_info, item):
    test_number = monkey_info['DivideByTestNumber']
    if item % test_number == 0:
        return monkey_info['TrueThrowTarget']
    else:
        return monkey_info['FalseThrowTarget']

def throw_item(throwing_monkey, catching_monkey, item):
    throwing_monkey['items'].pop(0)
    catching_monkey['items'].append(item)
    return

if __name__ == "__main__":
    main()