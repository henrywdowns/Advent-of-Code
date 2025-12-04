from aocd_api import AOCD
import numpy as np

# brute force baby here we go

puzzle = AOCD(4)
data = puzzle.get_list('\n')
rows = len(data)
cols = len(data[0])
dirs = [
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
            current_coords = [row,col]
            if data[row][col] == '@':
                current_coords_neighbor_count = 0 
                for dir in dirs: 
                    dir_neighbor = np.array(current_coords) + np.array(dir)
                    dir_neighbor = dir_neighbor.tolist()
                    if 0 <= dir_neighbor[0] < rows and 0 <= dir_neighbor[1] < cols:
                        if data[dir_neighbor[0]][dir_neighbor[1]] == '@': 
                            current_coords_neighbor_count += 1
                        else:
                            pass
                if current_coords_neighbor_count < 4:
                    sub_total += 1
                    mockup[row].append('.')
                else:
                    mockup[row].append('@')
            else:
                mockup[row].append('.') 
    grand_total += sub_total
    last_st = sub_total
    sub_total = 0
    data = mockup
    mockup = [[] for x in range(len(data))]
print(grand_total)
# puzzle.submit_answer(grand_total)