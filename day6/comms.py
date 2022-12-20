import sys,os

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        return file_content.read()

content = read_file("input.txt")
counter = 0

while counter < (len(content)):
    end_of_slice = counter + 4
    string = content[counter:end_of_slice]
    
    counter += 1

    print(string)