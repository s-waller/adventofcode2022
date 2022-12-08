import os,sys

sum = 0
elf_number = 0
most_snacks = 0
second_most_snacks = 0
third_most_snacks = 0
greedy_elf =0
second_greedy_elf = 0
third_greedy_elf = 0

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
                third_most_snacks = second_most_snacks
                second_most_snacks = most_snacks
                most_snacks = sum
                third_greedy_elf = second_greedy_elf
                second_greedy_elf = greedy_elf
                greedy_elf = elf
                print (greedy_elf + " has the most snacks with " + str(most_snacks))
            sum = 0
print (greedy_elf + " has the most snacks with " + str(most_snacks))
print (second_greedy_elf + " has the second most snacks with " + str(second_most_snacks))
print (third_greedy_elf + " has the third most snacks with " + str(third_most_snacks))
print ("Total calories of top 3 elves: " + str(most_snacks + second_most_snacks + third_most_snacks))
file_content.close()