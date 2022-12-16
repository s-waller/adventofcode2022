import sys,os,re,collections

def read_file(file):
    with open(os.path.join(sys.path[0], file), "r") as file_content:
        return file_content.readlines()

def get_starting_positions(crate_info):
    return re.findall('....?',crate_info)

def create_list(starting_position_line):
    list = []
    for i in starting_position_line:
        list += i[1]
    return list

def contains_numbers(line_input):
    return bool(re.search(r'\d', line_input))

def parse_instructions(line):
    move_count = (re.search('move (\d+)', line)).group(1)
    from_column_number = (re.search('from (\d+)', line)).group(1)
    to_column_number = (re.search('to (\d+)', line)).group(1)
    return [move_count,from_column_number,to_column_number]

def move_blocks(number_of_moves,from_stack,to_stack):
    number_of_moves_var = number_of_moves
    from_stack_var = from_stack
    to_stack_var = to_stack
    for i in range(int(number_of_moves_var)):
        block_to_move = list(crate_columns.items())[int(from_stack_var) -1][1][-1]
        (list(crate_columns.items())[int(from_stack_var) -1][1]).pop()
        (list(crate_columns.items())[int(to_stack_var) -1][1]).append(block_to_move)
    return

def check_crate_positions():
    #print("\033c\033[3J", end='')
    print("\033c")
    for index in crate_columns.keys():
        print(crate_columns[index])
    return

# build dictionary 
crate_columns = collections.OrderedDict()
length_of_column = 0
for line in (read_file("cratesparsetest.txt")):
    if line == '\n':
        break
    elif contains_numbers(line):
        number_list = re.findall('\d', line)
        for i in number_list:
            crate_columns['column_%s' % i] = [None] * length_of_column
    else:
        length_of_column += 1
        continue

row_counter = 0
column_starting_height = length_of_column - 1
# add starting positions to dictionary
for line in (read_file("cratesparsetest.txt")):
    if line == '\n':
        break
    elif contains_numbers(line):
        continue
    else:
        column_counter = 0
        starting_positions = (get_starting_positions(line))
        crate_position_row = create_list(starting_positions)
        for i in crate_position_row:
            list(crate_columns.items())[column_counter][1][column_starting_height] = i
            column_counter += 1
        column_starting_height -= 1
        row_counter += 1

# strip empty placeholder list values
list_indexer = 0
for index in crate_columns.keys():
    stripped_list = (list([x for x in list(crate_columns.items())[list_indexer][1] if x.strip()]))
    list_indexer += 1
    crate_columns[index] = stripped_list
    #print(crate_columns[index])

# checkpoint - block positions at beginning
check_crate_positions()

# run through actions
for line in (read_file("cratesparsetest.txt")):
    if line.startswith("move"):
#        (list(crate_columns.items())[0][1]).append("D")
#        (list(crate_columns.items())[0][1]).remove("D")
        #print(list(crate_columns.items())[0][1][-1])
        instructions = parse_instructions(line)
        move_blocks(instructions[0],instructions[1],instructions[2])
        check_crate_positions()
        #sleep
    else:
        continue

# check top crate in each column