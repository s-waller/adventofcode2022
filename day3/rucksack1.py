import os,sys

def check_priority(letter):
    if letter.islower():
        return ord(letter) - 96
    if letter.isupper():
        return ord(letter) - 38

def split_string(input):
    return input[:len(input)//2],input[len(input)//2:]

def find_common_chars(string1,string2):
    return ''.join(set(string1).intersection(string2))

priority_total = 0

with open(os.path.join(sys.path[0], "input.txt"), "r") as file_content:
    lines = file_content.readlines()
    for i in lines:
        string = str(i).strip()
        compartments = split_string(string)
        common_items = find_common_chars(compartments[0],compartments[1])
        for item in list(common_items):
            priority_total += check_priority(item)

print(priority_total)