import sys,os,itertools

grid = [['H']]
H_positions = [[0,0]]
T1_positions = [[0,0]]
T2_positions = [[0,0]]
T3_positions = [[0,0]]
T4_positions = [[0,0]]
T5_positions = [[0,0]]
T6_positions = [[0,0]]
T7_positions = [[0,0]]
T8_positions = [[0,0]]
T9_positions = [[0,0]]

all_knots = [H_positions, T1_positions, T2_positions, T3_positions, T4_positions, T5_positions, T6_positions, T7_positions, T8_positions, T9_positions] 

def main():
    content = read_file("input.txt")
    #print(*content, sep='\n')

    # loop through moves
    for instruction in content:
        direction = instruction[0]
        multiplier = instruction[1]
        for i in range(int(multiplier)):
            move_selector(direction)
            for pair in itertools.pairwise(all_knots):
                if touch_check(pair[0], pair[1]):
                    continue
                else:
                    move_T(pair[0], pair[1])

    unique_data = [list(x) for x in set(tuple(x) for x in T9_positions)]
    print(len(unique_data))
            
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
        for knot_positions in all_knots:
            for position in knot_positions: # to stablise T_positions values against the expanding grid
                position[1] = position[1] + 1
        H = H_positions[-1]
        H_positions.append([H[0],H[1] - 1])
    else:
        grid[h_location[0][0]][h_location[0][1]] = ' '
        grid[h_location[0][0]][h_location[0][1] - 1] = 'H'
        H = H_positions[-1]
        H_positions.append([H[0],H[1] - 1])
    return

def move_right():
    h_location = find_knot('H')
    if h_location[0][1] == len(grid[0]) -1:
        for row in range(len(grid)):
            grid[row].append(' ')
        updated_h_location = find_knot('H')
        grid[updated_h_location[0][0]][updated_h_location[0][1]] = ' '
        grid[updated_h_location[0][0]][updated_h_location[0][1] + 1] = 'H'
        H = H_positions[-1]
        H_positions.append([H[0],H[1] + 1])
    else:
        grid[h_location[0][0]][h_location[0][1]] = ' '
        grid[h_location[0][0]][h_location[0][1] + 1] = 'H'
        H = H_positions[-1]
        H_positions.append([H[0],H[1] + 1])
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
        for knot_positions in all_knots:
            for position in knot_positions: # to stablise T_positions values against the expanding grid
                position[0] = position[0] + 1
        H = H_positions[-1]
        H_positions.append([H[0] - 1,H[1]])
    else:
        grid[h_location[0][0]][h_location[0][1]] = ' '
        grid[h_location[0][0] - 1][h_location[0][1]] = 'H'
        H = H_positions[-1]
        H_positions.append([H[0] - 1,H[1]])
    return

def move_down():
    h_location = find_knot('H')
    if h_location[0][0] == len(grid) -1:
        grid.append([])
        for i in range(len(grid[-2])):
            grid[-1].append(' ')
        updated_h_location = find_knot('H')
        grid[updated_h_location[0][0]][updated_h_location[0][1]] = ' '
        grid[updated_h_location[0][0] + 1][updated_h_location[0][1]] = 'H'
        H = H_positions[-1]
        H_positions.append([H[0] + 1,H[1]])
    else:
        grid[h_location[0][0]][h_location[0][1]] = ' '
        grid[h_location[0][0] + 1][h_location[0][1]] = 'H'
        H = H_positions[-1]
        H_positions.append([H[0] + 1,H[1]])
    return

def touch_check(leader, follower):
    #H = find_knot('H')
    H = leader[-1]
    T = follower[-1]
    if (H[0] == T[0] or H[0] == T[0] + 1 or H[0] == T[0] - 1) and (H[1] == T[1] or H[1] == T[1] + 1 or H[1] == T[1] - 1):
        return True
    else:
        return False

def move_T(leader, follower):
    #H = find_knot('H')
    H = leader[-1]
    T = follower[-1]
    # move left
    if (H[0] == T[0]) and (H[1] == T[1] - 2):
        follower.append([T[0],T[1] - 1])
    # move right
    elif (H[0] == T[0]) and (H[1] == T[1] + 2):
        follower.append([T[0],T[1] + 1])
    # move up
    elif (H[0] == T[0] - 2) and (H[1] == T[1]):
        follower.append([T[0] - 1,T[1]])
    # move down
    elif (H[0] == T[0] + 2) and (H[1] == T[1]):
        follower.append([T[0] + 1,T[1]])
    # move left up
    elif ((H[0] == T[0] - 1) and (H[1] == T[1] - 2)) or ((H[0] == T[0] - 2) and (H[1] == T[1] - 1)):
        follower.append([T[0] - 1,T[1] - 1])
    # move left down
    elif ((H[0] == T[0] + 1) and (H[1] == T[1] - 2)) or ((H[0] == T[0] + 2) and (H[1] == T[1] - 1)):
        follower.append([T[0] + 1,T[1] - 1])
    # move right up
    elif ((H[0] == T[0] - 2) and (H[1] == T[1] + 1)) or ((H[0] == T[0] - 1) and (H[1] == T[1] + 2)):
        follower.append([T[0] - 1,T[1] + 1])
    # move right down
    elif ((H[0] == T[0] + 2) and (H[1] == T[1] + 1)) or ((H[0] == T[0] + 1) and (H[1] == T[1] + 2)):
        follower.append([T[0] + 1,T[1] + 1])

if __name__ == "__main__":
    main()