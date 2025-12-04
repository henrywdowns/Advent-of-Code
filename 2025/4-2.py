from aocd_api import AOCD
import numpy as np

puzzle = AOCD(4)

test_data = [
    '..@@.@@@@.',
    '@@@.@.@.@@',
    '@@@@@.@.@@',
    '@.@@@@..@.',
    '@@.@@@@.@@',
    '.@@@@@@@.@',
    '.@.@.@.@@@',
    '@.@@@.@@@@',
    '.@@@@@@@@.',
    '@.@.@@@.@.'
]

data = puzzle.get_list('\n')

# data = test_data

# for line in test_data:
#     print(list(line))
# print(' ')

rows = len(data)
cols = len(data[0])

dirs = [# every relative coord to check
    (-1,-1),(0,-1),(1,-1),
    (-1,0),(1,0),
    (-1,1),(0,1),(1,1)
]

mockup = [[] for x in range(len(data))]

loop_protection = 0

last_st = 1
grand_total = 0
sub_total = 0
while last_st > 0 and loop_protection < 50:
    loop_protection += 1
    for row in range(rows):
        for col in range(cols):
            # now sweeping left to right in each row
            current_coords = [row,col]
            if data[row][col] == '@': # only need to scan around @ signs
                current_coords_neighbor_count = 0 # declare a var to increment
                # print(f'Current coords: {current_coords} -- Symbol check: {data[row][col]}')
                for dir in dirs: # iterate through the possible directions, convert to arrays so i can easily add dirs to current coords
                    dir_neighbor = np.array(current_coords) + np.array(dir)
                    dir_neighbor = dir_neighbor.tolist()
                    # print(f'Dir neighbor coords: {dir_neighbor}')
                    if 0 <= dir_neighbor[0] < rows and 0 <= dir_neighbor[1] < cols:
                        if data[dir_neighbor[0]][dir_neighbor[1]] == '@': # if the neighbor coords exist on the grid and is @, increment count
                            current_coords_neighbor_count += 1
                            # print(f'    Found @ at {dir_neighbor}')
                        elif data[dir_neighbor[0]][dir_neighbor[1]] == '.': # if it's not @, don't increment
                            pass
                        else:
                            raise ValueError # if it's something else, something is truly wrong
                if current_coords_neighbor_count < 4:
                    sub_total += 1
                    mockup[row].append('.') # if the current coords are @ and removable, add a '.' to mockup for the next round
                else:
                    mockup[row].append('@')
            else:
                mockup[row].append('.') # if it's not @, it's empty space and we can add '.' to the mockup immediately
    grand_total += sub_total
    last_st = sub_total
    sub_total = 0
    data = mockup
    mockup = [[] for x in range(len(data))]
# for x in data:
#     print(list(x))
# print(' ')
# # for mockup_row in mockup:
# #     print(mockup_row)

print(grand_total)
puzzle.submit_answer(grand_total)