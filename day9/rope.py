import sys,os

grid = [['H']]

def main():
    content = read_file("input.txt")
    #print(*content, sep='\n')

    # loop through moves
    for instruction in content:
        direction = instruction[0]
        multiplier = instruction[1]
        move_selector(direction)
    # create a function for each move

    # expand grid if required - add a check on move

    # make T follow H

    # track history of T's position

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        list_of_strings = file_content.read().split('\n')
        result = [i.split() for i in list_of_strings]
        return result

def move_selector(input):
    if input == 'L':
        move_left()
    if input == 'R':
        move_right()
    if input == 'U':
        move_up()
    if input == 'D':
        move_down()

def move_left():
    # if H index == 0 (todo)
    for row in range(len(grid)):
        grid[row].insert(0, ' ')
    return

def move_right():
    # if H index == -1 (todo)
    for row in range(len(grid)):
        grid[row].append(' ')
    return

def move_up():
    # if H index == 0 (todo)
    grid.insert(0, [])
    for i in range(len(grid[1])):
        grid[0].append(' ')
    return

def move_down():
    # if H index == -1 (todo)
    grid.append([])
    for i in range(len(grid[-2])):
        grid[-1].append(' ')
    return

def tail_checkpoint():
    return

if __name__ == "__main__":
    main()