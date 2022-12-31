import sys,os

X = 1
cycle = 1
cycle_checkpoints = []

def main():
    content = read_file("input.txt")
    for instruction in content:
        run_instruction(instruction)
    signal_result = sum(cycle_checkpoints)
    print(signal_result)

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
    if ((number - 20) % 40 == 0):
        cycle_checkpoints.append(int(X) * int(cycle))

if __name__ == "__main__":
    main()