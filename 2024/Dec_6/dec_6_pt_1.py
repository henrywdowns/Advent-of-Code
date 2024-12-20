import numpy as np

data = open('Dec_6/input.txt','r').read().strip().split('\n')

split_data = [list(line) for line in data]

current_dir = (-1,0)
obstacles = []
current_loc = (0,0)

def main():
    global current_dir, current_loc
    find_obstacles()
    print(f'Starting loc: {current_loc}')
    
    split_data[current_loc[0]][current_loc[1]] = 'X'  # Mark starting position
    
    while True:
        print(f'Current loc: {current_loc}, Current dir: {current_dir}')
        target_pos = get_next(current_loc, current_dir)
        
        if target_pos == 'Out of bounds':
            print("Reached out of bounds. Terminating.")
            break
        elif target_pos in obstacles:
            print(f"Obstacle at {target_pos}. Turning right.")
            current_dir = turn_right(current_dir)
        else:
            current_loc = target_pos
            split_data[current_loc[0]][current_loc[1]] = 'X'
        
        print(f'New location: {current_loc}')
        
        # Optional: Add a way to visualize each step
        # print_grid()
        # input("Press Enter to continue...")

    final_count = sum(row.count('X') for row in split_data)
    print_grid()
    print(f"Final count of visited positions: {final_count}")



def find_obstacles():
    global current_loc
    for i, row in enumerate(split_data):
        for j, item in enumerate(row):
            if item == '#':
                obstacles.append((i,j))
            elif item == '^':
                current_loc = (i,j)
                print(f'Current loc: {current_loc}')
    print(f'There are {len(obstacles)} obstacles.')

def get_next(loc, dir):
    print(f'Loc: {loc} -- dir: {dir}')
    target_coords = (loc[0]+dir[0], loc[1]+dir[1])
    if (0 <= target_coords[0] < len(split_data) and 
        0 <= target_coords[1] < len(split_data[0])):
        print(f'Target position: {target_coords}')
        print(f'Target position value: {split_data[target_coords[0]][target_coords[1]]}')
        return target_coords
    else:
        return 'Out of bounds'

def turn_right(dir):
    print(f'Turning right')
    new_dir = (0,0)
    match dir:
        case (-1,0):
            new_dir = (0,1)
        case (0,1):
            new_dir = (1,0)
        case (1,0):
            new_dir = (0,-1)
        case (0,-1):
            new_dir = (-1,0)
    return new_dir

def move(loc,dir):
    global current_loc
    x,y = dir[0],dir[1]
    a,b = loc[0],loc[1]
    current_loc = (x+a,y+b)

def print_grid():
    header = [str(x) for x in range(len(split_data))]
    header.insert(0,' ')
    print(header,'\n')
    for i, line in enumerate(split_data):
        grid_line = line
        line.insert(0,str(i))
        print(line)

if __name__ == '__main__':
    main()