import os,sys

priority_total = 0

with open(os.path.join(sys.path[0], "input.txt"), "r") as file_content:
    lines = file_content.readlines()
    group = []
    counter = 0
    for i in lines:
        string = str(i).strip()
        group.append(string)
        if len(group) == 3:

            


            group = []
        
print(len(group))