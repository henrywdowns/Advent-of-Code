from aocd_api import AOCD
import numpy as np

puzzle = AOCD(4)
data = puzzle.get_list('\n')
rows = len(data)
cols = len(data[0])

dirs = [
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
        current_coords = [row,col]
        if data[row][col] == '@': 
            current_coords_neighbor_count = 0
            for dir in dirs:
                dir_neighbor = np.array(current_coords) + np.array(dir)
                dir_neighbor = dir_neighbor.tolist()
                if 0 <= dir_neighbor[0] < rows and 0 <= dir_neighbor[1] < cols:
                    if data[dir_neighbor[0]][dir_neighbor[1]] == '@': 
                        current_coords_neighbor_count += 1
                    elif data[dir_neighbor[0]][dir_neighbor[1]] == '.': 
                        pass
                    else:
                        raise ValueError
            mockup[row].append(str(current_coords_neighbor_count))
            if current_coords_neighbor_count < 4:
                grand_total += 1
        else:
            mockup[row].append('.')
print(grand_total)
puzzle.submit_answer(grand_total)