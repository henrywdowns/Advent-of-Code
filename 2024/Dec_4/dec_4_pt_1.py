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
        if type(line) == list:
            line = ''.join(line)
            print(line)
        lr_list = re.findall('(XMAS|SAMX)',line)
        running_total += len(lr_list)
    return running_total

def DiagonalOrder(arr,dir):
    rows, cols = len(data),len(data[0])
    diagonal_matrix = [[] for i in range (rows + cols - 1)]
    for i in range(cols):
        for j in range(rows):
            combine_i_j = 0
            if dir == 'down-left':
                combine_i_j = (i + j)
            elif dir == 'up-right':
                combine_i_j = (cols - 1 - j) + i
            diagonal_matrix[combine_i_j].append(arr[i][j])
        
    return diagonal_matrix
    
down_left = DiagonalOrder(data,'down-left')
up_right = DiagonalOrder(data,'up-right')

for axis in [horizontal,vertical,down_left,up_right]:
    dir_count = count_matches(axis)
    print(dir_count)
    xmas_count += dir_count

print(xmas_count)