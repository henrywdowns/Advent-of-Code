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

mockup = []

for x in range(len(data)):
    mockup.append([])

last_gt = 0
grand_total = 0
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
            mockup[row].append(str(current_coords_neighbor_count)) # if the current coords are @, we add the count to the mockup for debugging
            if current_coords_neighbor_count < 4:
                # grand_total += current_coords_neighbor_count # also, we add the count to the grand total if it's below 4
                grand_total += 1
        else:
            mockup[row].append('.') # if it's not @, it's empty space and we can add '.' to the mockup immediately

# for x in data:
#     print(list(x))
# print(' ')
# for mockup_row in mockup:
#     print(mockup_row)

print(grand_total)
puzzle.submit_answer(grand_total)