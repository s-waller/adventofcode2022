import os,sys

# create dictionary of priorities 
# 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s)
#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.

def check_priority(letter):
    if letter.islower():
        return ord(letter) - 96
    if letter.isupper():
        return ord(letter) - 38

def split_string(input):
    return input[:len(input)//2],input[len(input)//2:]

def find_common_chars(string1,string2):
    return ''.join(set(string1).intersection(string2))

#get rucksacks, 1 per line
with open(os.path.join(sys.path[0], "input.txt"), "r") as file_content:
    lines = file_content.readlines()
    for i in lines:
        string = str(i).strip()
        compartments = split_string(string)
        common_items = find_common_chars(compartments[0],compartments[1])

#divide rucksacks into compartments

#find any items that are in both compartments

#get priority of items that were found in both

#total priority