import sys,os

def main():
    content = read_file("input.txt")
    #print(*content, sep='\n')

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        list_of_strings = file_content.read().split('\n')
        result = [i.split() for i in list_of_strings]
        return result

if __name__ == "__main__":
    main()