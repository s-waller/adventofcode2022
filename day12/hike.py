import sys
import os
import string
import random

def main():
    mapped_area = read_file("sample.txt")
    print(len(mapped_area[0]))
    walked_area = []
    string = ("." * 101)
    for i in range(41):
        walked_area.append(string)
    print(*walked_area, sep='\n')
    successful_paths = []
    current_steps = []
    stepped_ground = set()
    print(*mapped_area, sep='\n')
    start_location = find_position('S', mapped_area)
    target_location = find_position('E', mapped_area)
    print(start_location, target_location)
    current_location = current_steps[-1] if current_steps else start_location
    current_steps.append(current_location)

    #walk_paths(mapped_area, options, visited, dfs_traversal)

    while current_location != target_location:
        current_location = current_steps[-1]
        if current_location == target_location:
            successful_paths.append(current_steps)
            summit_reached()
        options = scan_directions(current_location, mapped_area)
        if options:
            current_location = move(current_location, random.choice(options), current_steps)
            #current_location = move(current_location, north, current_steps)
            stepped_ground.add(tuple(current_location))
        else:
            dead_end()
def walk_paths(mapped_area, options, visited, dfs_traversal):
    for direction in options:
        
        walk_paths(mapped_area, options, visited, dfs_traversal)

visited = set()
dfs_traversal = list()

def walk_paths(graph, options, visited, dfs_traversal):    
    if direction not in visited:
        dfs_traversal.append(source)
        visited.add(source)

        for neighbor_node in graph[source]:
            dfs(fff, neighbor_node, visited, dfs_traversal)

    return dfs_traversal



    #for direction in options:
        #move_selector(current_location, direction)

            
def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        list_of_strings = file_content.read().split('\n')
        #result = [list(i) for i in list_of_strings]
        return list_of_strings #result

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

def valid_coordinates(coordinates, area):
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

def scan_directions(current_location, mapped_area):
    possible_directions = []
    for direction in (north, south, east, west):
        direction_coordinates = direction(current_location)
        if valid_coordinates(direction_coordinates, mapped_area)
            if can_climb(current_location, direction_coordinates, mapped_area)
                possible_directions.append(direction)
    return possible_directions

def dead_end():
    print("Dead End Reached")
    return 

def summit_reached():
    print("Summit Reached")
    return

if __name__ == "__main__":
    main()