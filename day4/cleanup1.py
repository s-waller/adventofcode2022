import sys,os

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        return file_content.readlines()

def separate_pair (string):
    return string.split(",")

def get_elf_zone_range(pair_list,elf_index):
    return pair_list[elf_index].split("-")

def list_elf_zones(elf_zones_shorthand):
    return list(range(int(elf_zones_shorthand[0]),(int(elf_zones_shorthand[-1]) + 1)))

count = 0

for line in (read_file("input.txt")):
    elf_pair = (str(line).strip())
    pair_list = separate_pair(elf_pair)

# get list of elf1 zones
    elf1_zone_short = get_elf_zone_range(pair_list,0)
    elf1_zones = list_elf_zones(elf1_zone_short)

# get list of elf2 zones
    elf2_zone_short = get_elf_zone_range(pair_list,-1)
    elf2_zones = list_elf_zones(elf2_zone_short)

    if(set(elf1_zones).issubset(set(elf2_zones))) or (set(elf2_zones).issubset(set(elf1_zones))):
        count += 1
print(count)