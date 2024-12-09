import re
import numpy as np

data = open('Dec_4/input.txt','r').read().strip().split('\n')

diameter = 140
xmas_count = 0

array_data = np.array([list(row) for row in data])
horizontal = data
vertical = (np.transpose(array_data)).tolist()

def count_matches(input_data):
    running_total = 0
    for line in input_data:
        if isinstance(line, list):
            line = ''.join(line)
        lr_list = re.findall(r"(?=(XMAS|SAMX))", line)
        running_total += len(lr_list)
    return running_total

def DiagonalOrder(arr,dir):
    rows, cols = len(data),len(data[0])
    diagonal_matrix = [[] for i in range (rows + cols - 1)]
    for i in range(cols):
        for j in range(rows):
            combine_i_j = (i + j)
            if dir == 'down-left':
                diagonal_matrix[combine_i_j].append(arr[i][j])
            elif dir == 'up-right':
                diagonal_matrix[combine_i_j].append(arr[i][cols-1-j])    
    return diagonal_matrix
    
down_left = DiagonalOrder(data,'down-left')
up_right = DiagonalOrder(data,'up-right')

for axis in [horizontal,vertical,down_left,up_right]:
    dir_count = count_matches(axis)
    #print(dir_count)
    xmas_count += dir_count

print(f'xmas count: {xmas_count}')