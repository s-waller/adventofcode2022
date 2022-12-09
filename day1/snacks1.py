import os,sys

sum = 0
elf_number = 0
most_snacks = 0

with open(os.path.join(sys.path[0], "input.txt"), "r") as file_content:
    lines = file_content.readlines()
    for i in lines:
        i = str(i).strip()
        if i.isdigit():
            sum += int(i)
        else:
            elf_number += 1
            elf = "elf" + str(elf_number)
            snacks = str(sum)
            print (elf + ": " + snacks)
            if sum > most_snacks:
                most_snacks = sum
                greedy_elf = elf
                print (greedy_elf + " has the most snacks with " + str(most_snacks))
            sum = 0
print (greedy_elf + " has the most snacks with " + str(most_snacks))
file_content.close()