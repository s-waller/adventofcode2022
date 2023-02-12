import os
import sys


def main():
    rocks = parse_file("sample.txt")
    return


def parse_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        list = file_content.read().split('\n')
        for i in list:
            list[list.index(i)] = i.split(' -> ')
        for i in list:
            for j in i:
                i[i.index(j)] = j.split(',')
        return list


if __name__ == "__main__":
    main()