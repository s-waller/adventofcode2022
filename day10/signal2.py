import sys,os

X = 1
cycle = 1
cycle_checkpoints = []
crt_screen = [[],[],[],[],[],[]]
sprite_position = ['#','#','#']

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
        cycle_check(cycle)

    elif input[0] == 'addx':
        draw_pixel()
        cycle = cycle + 1
        cycle_check(cycle)
        draw_pixel()
        cycle = cycle + 1
        X = X + int(input[1])
        cycle_check(cycle)

def cycle_check(number):
    if ((number != 0) and (number % 40 == 0)):
        cycle_checkpoints.append(int(X) * int(cycle))

def draw_pixel():
    row = check_row()
    if (row[2] - row[1]) == X or (row[2] - row[1]) == X + 1 or (row[2] - row[1]) == X - 1:
        crt_screen[row[0]].append('#')
    else:
        crt_screen[row[0]].append('.')

def check_row():
    if cycle <= 40:
        return 0, 0, cycle
    elif cycle >= 41 and cycle <= 80:
        return 1, 40, cycle
    elif cycle >= 81 and cycle <= 120:
        return 2, 80, cycle
    elif cycle >= 121 and cycle <= 160:
        return 3, 120, cycle
    elif cycle >= 161 and cycle <= 200:
        return 4, 160, cycle
    elif cycle >= 201 and cycle <= 240:
        return 5, 200, cycle

if __name__ == "__main__":
    main()