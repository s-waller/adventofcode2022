import sys
import os
import string
import random
import time
import copy
from collections import deque

def main():
    mapped_area = read_file("input.txt")
    walked_area = []
    string = ("#" * len(mapped_area[0]))
    for i in range(len(mapped_area)):
        walked_area.append(string)
    current_steps = []
    #print(*mapped_area, sep='\n')
    start_location = find_position('S', mapped_area)
    target_location = find_position('E', mapped_area)
    current_location = current_steps[-1] if current_steps else start_location
    current_steps.append(current_location)
    walked_area_refresh = copy.deepcopy(walked_area)
    
    print(breadth_first_search(start_location, target_location, mapped_area, walked_area, walked_area_refresh))

def breadth_first_search(start, end, mapped_area, walked_area, refresh):
    queue = deque([start])
    visited = {start}
    trace = {}

    while queue:
        print_status(visited, end, walked_area, refresh)
        vertex = queue.popleft()
        options = scan_directions(vertex, mapped_area, visited)
        if vertex == end:
            break

        for direction in options:
            neighbor = direction(vertex)
            if neighbor not in visited:
                visited.add(neighbor)
                trace[neighbor] = vertex
                queue.append(neighbor)

    path = [end]
    while path[-1] != start:
        last_node = path[-1]
        next_node = trace[last_node]
        path.append(next_node)
    
    return path[::-1]

def print_status(visited, target_location, walked_area, refresh):
    walked_area = copy.deepcopy(refresh)
    walked_area[target_location[0]] = walked_area[target_location[0]][:target_location[1]] + "E" + walked_area[target_location[0]][target_location[1] + 1:]
    for step in visited:
        walked_area[step[0]] = walked_area[step[0]][:step[1]] + "." + walked_area[step[0]][step[1] + 1:]
        
    os.system('')
    print(*walked_area, sep='\n')
    #time.sleep(0.005)
    #print("\033c")
    print("\033[42F")
    
def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        list_of_strings = file_content.read().split('\n')
        return list_of_strings

def find_position(input, mapped_area):
    return tuple([[i, location.index(input)]
    for i, location in enumerate(mapped_area)
    if input in location][0])

def west(current_location):
    location = (current_location[0],current_location[1] - 1)
    return location

def east(current_location):
    location = (current_location[0],current_location[1] + 1)
    return location

def north(current_location):
    location = (current_location[0] - 1,current_location[1])
    return location

def south(current_location):
    location = (current_location[0] + 1,current_location[1])
    return location

def move(current_location, next_step, current_steps):
    new_location = next_step(current_location)
    current_steps.append(new_location)
    return new_location

def check_elevation(location, mapped_area):
    elevation = mapped_area[location[0]][location[1]]
    if elevation == 'S':
        elevation = 'a'
    if elevation == 'E':
        elevation = 'z'
    return elevation

def valid_coordinates(coordinates, area, visited):
    if tuple(coordinates) in visited:
        return False
    if coordinates[0] >= len(area) or coordinates[1] >= len(area[0]):
        return False
    if coordinates[0] < 0 or coordinates[1] < 0: # negative values would cause the mover to teleport to the other end of the map
        return False
    return True

def can_climb(current_location, target_location, area):
    elevations = list(string.ascii_lowercase)
    current_elevation = check_elevation(current_location, area)
    current_elevations_index = elevations.index(current_elevation)
    if check_elevation(target_location, area) in elevations[0:(current_elevations_index + 2)]:
        return True
    else:
        return False

def scan_directions(current_location, mapped_area, visited):
    possible_directions = []
    for direction in (north, south, east, west):
        direction_coordinates = direction(current_location)
        if valid_coordinates(direction_coordinates, mapped_area, visited):
            if can_climb(current_location, direction_coordinates, mapped_area):
                possible_directions.append(direction)
    return possible_directions

def dead_end(coordinates, dead_ends):
    dead_ends.add(tuple(coordinates))
    return 

def summit_reached(current_steps):
    print("Summit reached in " + str(len(current_steps)) + " steps.")
    return

if __name__ == "__main__":
    main()