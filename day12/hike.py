import sys
import os
import string
import random

def main():
    mapped_area = read_file("input.txt")
    successful_paths = []
    current_steps = [] 
    print(*mapped_area, sep='\n')
    start_location = find_position('S', mapped_area)
    target_location = find_position('E', mapped_area)
    print(start_location, target_location)
    current_location = current_steps[-1] if current_steps else start_location
    current_steps.append(current_location)

    while current_location != target_location:
        current_location = current_steps[-1]
        if current_location == target_location:
            successful_paths.append(current_steps)
        options = scan_directions(current_location, mapped_area)
        current_location = move(current_location, random.choice(options), current_steps)
        #current_location = move(current_location, north, current_steps)


    #for direction in options:
        #move_selector(current_location, direction)

            
def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        list_of_strings = file_content.read().split('\n')
        result = [list(i) for i in list_of_strings]
        return result

def find_position(input, mapped_area):
    return [[i, location.index(input)]
    for i, location in enumerate(mapped_area)
    if input in location][0]

def west(current_location):
    location = [current_location[0],current_location[1] - 1]
    return location

def east(current_location):
    location = [current_location[0],current_location[1] + 1]
    return location

def north(current_location):
    location = [current_location[0] - 1,current_location[1]]
    return location

def south(current_location):
    location = [current_location[0] + 1,current_location[1]]
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
        elevation == 'z'
    return elevation

def scan_directions(current_location, mapped_area):
    possible_directions = []
    elevations = list(string.ascii_lowercase)
    current_elevation = check_elevation(current_location, mapped_area)
    current_elevations_index = elevations.index(current_elevation)
    for direction in (north, south, east, west):
        if check_elevation(direction(current_location), mapped_area) in elevations[0:(current_elevations_index + 2)]:
            possible_directions.append(direction)
    return possible_directions

if __name__ == "__main__":
    main()