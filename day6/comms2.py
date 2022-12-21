import sys,os

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        return file_content.read()

def unique_characters(string):
    string_as_set = set(string)
    if(len(string_as_set) == len(string)):
        return True
    return False

content = read_file("input.txt")
counter = 0
unique_string_found = False

while unique_string_found == False:
    end_of_slice = counter + 14
    string = content[counter:end_of_slice]
    if (unique_characters(string)):
        unique_string_found = True
    counter += 1

print(end_of_slice)
print(string)