import sys,os

def main():
    content = read_file("input.txt")
    #print(*content, sep='\n')
    range_count = range(len(content))
    list_of_columns = get_columns(content)
    x_count = 0
    y_count = 0
    highest_scenic_score = 0

    for row in range_count:
        x_count = 0
        for tree in content[int(row)]:
            scenic_score = 0
            east_view = 0
            west_view = 0
            north_view = 0
            south_view = 0

            east_side = content[int(row)][int(x_count) + 1:]
            west_side = content[int(row)][:int(x_count)]
            north_side = list_of_columns[int(x_count)][:int(y_count)]
            south_side = list_of_columns[int(x_count)][int(y_count) + 1:]

            if west_side == [] or east_side == [] or north_side == [] or south_side == []:
                scenic_score = 0
            else:
                east_view = next((x for x, val in enumerate(east_side) if val >= tree), (len(east_side) - 1)) +1
                west_view = next((x for x, val in enumerate(list(reversed(west_side))) if val >= tree), (len(west_side) - 1)) + 1
                north_view = next((x for x, val in enumerate(list(reversed(north_side))) if val >= tree), (len(north_side) - 1)) + 1
                south_view = next((x for x, val in enumerate(south_side) if val >= tree), (len(south_side) - 1)) + 1

            scenic_score = east_view * west_view * north_view * south_view
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score
            x_count = x_count + 1
        y_count = y_count + 1
        
    print(highest_scenic_score)
    

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        list_of_strings = file_content.read().split('\n')
        result = [list(i) for i in list_of_strings]
        return result

def get_columns(input):
    columns = [[row[i] for row in input] for i in range(len(input))]
    return columns

if __name__ == "__main__":
    main()