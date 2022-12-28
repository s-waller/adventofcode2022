import sys,os

grid = [['H']]

def main():
    content = read_file("input.txt")
    #print(*content, sep='\n')

    # loop through moves
    for instruction in content:
        coordinates_H = find_knot('H')
        print(coordinates_H)
        direction = instruction[0]
        multiplier = instruction[1]
        for i in range(int(multiplier)):
            move_selector(direction)
        #print(grid)

    # create a function for each move

    # expand grid if required - add a check on move

    # make T follow H

    # track history of T's position

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        list_of_strings = file_content.read().split('\n')
        result = [i.split() for i in list_of_strings]
        return result

def find_knot(input):
    return [(i, location.index(input))
    for i, location in enumerate(grid)
    if input in location]

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
    h_location = find_knot('H')
    if h_location[0][1] == 0:
        for row in range(len(grid)):
            grid[row].insert(0, ' ')
        updated_h_location = find_knot('H')
        grid[updated_h_location[0][0]][updated_h_location[0][1]] = ' '
        grid[updated_h_location[0][0]][updated_h_location[0][1] - 1] = 'H'
    else:
        grid[h_location[0][0]][h_location[0][1]] = ' '
        grid[h_location[0][0]][h_location[0][1] - 1] = 'H'
    return

def move_right():
    h_location = find_knot('H')
    if h_location[0][1] == len(grid[0]) -1:
        for row in range(len(grid)):
            grid[row].append(' ')
        updated_h_location = find_knot('H')
        grid[updated_h_location[0][0]][updated_h_location[0][1]] = ' '
        grid[updated_h_location[0][0]][updated_h_location[0][1] + 1] = 'H'
    else:
        grid[h_location[0][0]][h_location[0][1]] = ' '
        grid[h_location[0][0]][h_location[0][1] + 1] = 'H'
    return

def move_up():
    h_location = find_knot('H')
    if h_location[0][0] == 0:
        grid.insert(0, [])
        for i in range(len(grid[1])):
            grid[0].append(' ')
        updated_h_location = find_knot('H')
        grid[updated_h_location[0][0]][updated_h_location[0][1]] = ' '
        grid[updated_h_location[0][0] - 1][updated_h_location[0][1]] = 'H'
    else:
        grid[h_location[0][0]][h_location[0][1]] = ' '
        grid[h_location[0][0] - 1][h_location[0][1]] = 'H'
    return

def move_down():
    h_location = find_knot('H')
    if h_location[0][0] == len(grid) -1:
        grid.append([])
        for i in range(len(grid[-2])):
            grid[-1].append(' ')
        updated_h_location = find_knot('H')
        grid[updated_h_location[0][0]][updated_h_location[0][1]] = ' '
        grid[updated_h_location[0][0] - 1][updated_h_location[0][1]] = 'H'
    else:
        grid[h_location[0][0]][h_location[0][1]] = ' '
        grid[h_location[0][0] + 1][h_location[0][1]] = 'H'
    return

def tail_checkpoint():
    return

if __name__ == "__main__":
    main()