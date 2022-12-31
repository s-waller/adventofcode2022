import sys,os,yaml

def main():
    content = read_file("input.txt")
    print(*content, sep='\n')

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        result = yaml.safe_load(file_content)
        return result

if __name__ == "__main__":
    main()