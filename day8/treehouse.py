import sys,os

def main():
    content = read_file("input.txt")
    #print(*content, sep='\n')
    range_count = range(len(content))
    list_of_columns = get_columns(content)
    x_count = 0
    y_count = 0
    visible_trees = 0
    
    for row in range_count:
        x_count = 0
        for tree in content[int(row)]:
            east_side = content[int(row)][int(x_count) + 1:]
            west_side = content[int(row)][:int(x_count)]
            north_side = list_of_columns[int(x_count)][:int(y_count)]
            south_side = list_of_columns[int(x_count)][int(y_count) + 1:]
            if west_side == [] or east_side == [] or north_side == [] or south_side == []:
                visible_trees = visible_trees + 1
            elif tree > max(west_side) or tree > max(east_side) or tree > max(north_side) or tree > max(south_side):
                visible_trees = visible_trees + 1

            x_count = x_count + 1
        y_count = y_count + 1
        
    print(visible_trees)
    

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