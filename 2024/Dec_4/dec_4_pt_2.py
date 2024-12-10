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
    print(len(arr))
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
down_left_no_pads = []
for i, line in enumerate(down_left):
    temp_diag_line = []
    str_space = (' '.join(line))
    for char in str_space:
        temp_diag_line.append(char)
    for x in range((279-len(temp_diag_line))//2):
        temp_diag_line.insert(0,' ')
        temp_diag_line.append(' ')
    p2_down_left.append(temp_diag_line)

def s_m_exchanger(letter):
        if letter.lower() == 'm':
            return 'S'
        elif letter.lower() == 's':
            return 'M'
        else:
            print("s_m_exchanger error")

def cross_mas(array):
    total = 0
    print(f'Array len: {len(array)}')
    # iterate through array, find an 'A'
    for i, row in enumerate(array):
        print(f'row len: {len(row)}')
        for j, letter in enumerate(row):
            if letter != ' ':
                print(f'letter: {letter}')
                if letter == 'A':
                    print(f'i: {i} -- j: {j}')
            if letter == 'A' and 1 < i < (len(array)-2) and 1 < j < (len(row)-2):
                #print(f'Array length: {len(array)} minus 2: {len(array)-2}\nRow length: {len(row)} minus 2: {len(row)-2}')
                up = array[i-2][j]
                down = array[i+2][j]
                left = array[i][j-2]
                right = array[i][j+2]
                print(f' -- Up: {up}')
                print(f' -- Down: {down}')
                print(f' -- Left: {left}')
                print(f' -- Right: {right}')
                if up == s_m_exchanger(down) and left == s_m_exchanger(right):
                    total += 1
                    continue
    return(total)

print(cross_mas(p2_down_left))