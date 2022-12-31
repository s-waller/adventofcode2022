import sys,os

X = 1
cycle = 1
cycle_checkpoints = []
crt_screen = [[],[],[],[],[],[]]

def main():
    content = read_file("input.txt")
    for instruction in content:
        run_instruction(instruction)
    for row in crt_screen:
        print(*row)

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        list_of_strings = file_content.read().split('\n')
        result = [i.split() for i in list_of_strings]
        return result

def run_instruction(input):
    global cycle, X
    if input[0] == 'noop':
        draw_pixel()
        cycle = cycle + 1

    elif input[0] == 'addx':
        draw_pixel()
        cycle = cycle + 1
        draw_pixel()
        cycle = cycle + 1
        X = X + int(input[1])

def draw_pixel():
    row = check_row()
    if (row[2] - row[1]) == X or (row[2] - row[1]) == X + 1 or (row[2] - row[1]) == X - 1:
        crt_screen[row[0]].append('#')
    else:
        crt_screen[row[0]].append('.')

def check_row():
    if cycle >= 1 and cycle <= 40:
        return 0, 1, cycle
    elif cycle >= 41 and cycle <= 80:
        return 1, 41, cycle
    elif cycle >= 81 and cycle <= 120:
        return 2, 81, cycle
    elif cycle >= 121 and cycle <= 160:
        return 3, 121, cycle
    elif cycle >= 161 and cycle <= 200:
        return 4, 161, cycle
    elif cycle >= 201 and cycle <= 240:
        return 5, 201, cycle

if __name__ == "__main__":
    main()