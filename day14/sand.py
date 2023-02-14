import os
import sys
import itertools


def main():
    rocks = parse_file("input.txt")
    rocks = calculate_rock_positions(rocks)
    sand_start_position = (500, 0)
    grid_sizes = get_grid_size(rocks)

    grid = create_grid(grid_sizes, rocks, sand_start_position)
    print(*grid, sep='\n')
    
    return


def parse_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        list = file_content.read().split('\n')
        new_list = []
        for item in list:
            if item not in new_list:
                new_list.append(item)
        list = new_list
        for i in list:
            list[list.index(i)] = i.split(' -> ')
        for i in list:
            for j in i:
                i[i.index(j)] = j.split(',')
        return list


def calculate_rock_positions(rocks):
    rock_positions = set()
    for list in rocks:
        for items in itertools.pairwise(list):
            first_item = items[0]
            second_item = items[1]
            first_item_horizontal = int(first_item[0])
            second_item_horizontal = int(second_item[0])
            first_item_vertical = int(first_item[1])
            second_item_vertical = int(second_item[1])

            # calculate the rock positions
            if first_item_horizontal == second_item_horizontal:
                for vertical in range(min(first_item_vertical, second_item_vertical), max(first_item_vertical, second_item_vertical) + 1):
                    rock_positions.add((first_item_horizontal, vertical))
            elif first_item_vertical == second_item_vertical:
                for horizontal in range(min(first_item_horizontal, second_item_horizontal), max(first_item_horizontal, second_item_horizontal) + 1):
                    rock_positions.add((horizontal, first_item_vertical))

    return rock_positions


def get_grid_size(rocks):

    grid_horizontal = min(rocks)[0], max(rocks)[0]
    grid_vertical = min(rocks, key = lambda t: t[1])[1], max(rocks, key = lambda t: t[1])[1]

    return grid_horizontal, grid_vertical


def rock_index(index_value, horizontal_start_index):
    new_index = index_value - horizontal_start_index
    return new_index


def create_grid(grid_sizes, rocks, sand_start):
    grid_height = grid_sizes[1][1]
    grid_width = grid_sizes[0][1] - grid_sizes[0][0]
    list = []
    for i in range(0, grid_height + 1):
        list.append([])
        for j in range(0, grid_width + 1):
            list[i] += "."
    list[sand_start[1]][rock_index(sand_start[0],grid_sizes[0][0])] = '+'
    for rock in rocks:
        list[rock[1]][rock_index(rock[0],grid_sizes[0][0])] = '#'
    return list

if __name__ == "__main__":
    main()