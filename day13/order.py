import sys
import os

def main():
    left = read_file("input.txt")
    right = read_file("input.txt")
    return

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        list_of_strings = file_content.read().split('\n')
        return list_of_strings
    
if __name__ == "__main__":
    main()