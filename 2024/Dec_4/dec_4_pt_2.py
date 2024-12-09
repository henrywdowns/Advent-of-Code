import re
import numpy as np

data = open('Dec_4/input.txt','r').read().strip().split('\n')

sq_width = 140
diag_width = 279
xmas_count = 0

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


# making a list with the diagonal 'centered'. all letters are 2 indices apart in both dimensions
p2_down_left = []
for i, line in enumerate(down_left[:5]):
    temp_diag_line = []
    str_space = (' '.join(line))
    for char in str_space:
        temp_diag_line.append(char)
    print(temp_diag_line)
    print(len(temp_diag_line))
    for x in range((279-len(temp_diag_line))//2):
        temp_diag_line.insert(0,' ')
        temp_diag_line.append(' ')
    p2_down_left.append(temp_diag_line)
    print(len(temp_diag_line))

# returns 1 if it picks it up cross-ways and 0 if not.
def cross_mas(array,coords):
    #coords should be a tuple with x/y axes    
    def s_m_exchanger(letter):
        if letter.lower() == 'm':
            return 'S'
        elif letter.lower() == 's':
            return 'M'
        else:
            print("s_m_exchanger error")
    #TODO: CHECK IF IN-BOUNDS
    if 2 <= coords[0] <= 276 and 2 <= coords[1] <= 276:    
        if array[coords[0]+2][coords[1]] == s_m_exchanger(array[coords[0]-2][coords[1]]):
            if array[coords[0]][coords[1]+2] == s_m_exchanger(array[coords[0]][coords[1]-2]):
                return 1
    return 0
            

cross_mas_count = 0
for i, row in enumerate(p2_down_left):
    for j, cols in enumerate(row):
        if cols.lower() == 'a':
            cross_mas_count += cross_mas(p2_down_left,(i,j))

print(cross_mas_count)


# for i, line in enumerate(down_left[:10]):
#     str_space = (' '.join(line))
#     print(str_space)
#     p2_down_left.append([])
#     for char in str_space:
#         p2_down_left[i].append(char)
#     p2_down_left[i]
#     line_len = len(line)
#     for x in range(diag_width-line_len):
#         p2_down_left.insert(0,' ')
#         p2_down_left.append(' ')
#     print(p2_down_left)


# print(f'xmas count: {xmas_count}')