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

def follow_instructions(move):
    return # crate_stack_change

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
        #print(crate_position_row)
        for i in crate_position_row:
            list(crate_columns.items())[column_counter][1][column_starting_height] = i
            column_counter += 1
        column_starting_height -= 1
        row_counter += 1
        print(crate_position_row)
#print(crate_columns)
#print(list(crate_columns.keys())[row_counter])
#print(list(crate_columns.items())[7][1][0])
#print(crate_position_row)

# run through actions
for line in (read_file("cratesparsetest.txt")):
    if line.startswith("move"):
        placeholder = 0 # follow instructions
    else:
        continue


print("\n")
print(crate_columns)
#crate_column_items = list(crate_columns.items())
#crate_column_keys = list(crate_columns.keys())
#print(crate_column_items[0])
#print(crate_column_keys[0])