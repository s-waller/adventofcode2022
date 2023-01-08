import sys,os,yaml

def main():
    content = read_file("input.txt")
    print(*content, sep='\n')

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        return file_content.read().split('\n')

if __name__ == "__main__":
    main()