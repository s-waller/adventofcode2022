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
        cycle = cycle + 1
        cycle_check(cycle)

    elif input[0] == 'addx':
        cycle = cycle + 1
        cycle_check(cycle)
        cycle = cycle + 1
        X = X + int(input[1])
        cycle_check(cycle)

def cycle_check(number):
    if ((number != 0) and (number % 40 == 0)):
        cycle_checkpoints.append(int(X) * int(cycle))

def check_row():
    if cycle <= 40:
        return crt_screen[0]
    elif cycle >= 41 and cycle <= 80:
        return crt_screen[1]
    elif cycle >= 81 and cycle <= 120:
        return crt_screen[2]
    elif cycle >= 121 and cycle <= 160:
        return crt_screen[3]
    elif cycle >= 161 and cycle <= 200:
        return crt_screen[4]
    elif cycle >= 201 and cycle <= 240:
        return crt_screen[5]

if __name__ == "__main__":
    main()