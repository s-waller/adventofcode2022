import os,sys

def check_priority(letter):
    if letter.islower():
        return ord(letter) - 96
    if letter.isupper():
        return ord(letter) - 38

def find_common_chars(string1,string2,string3):
    return ''.join(set(string1).intersection(string2,string3))

priority_total = 0

with open(os.path.join(sys.path[0], "input.txt"), "r") as file_content:
    lines = file_content.readlines()
    group = []
    counter = 0
    for i in lines:
        string = str(i).strip()
        group.append(string)
        if len(group) == 3:
            common_item = find_common_chars(group[0],group[1],group[2])
            priority_total += check_priority(common_item)
            group = []

print(priority_total)