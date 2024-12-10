import numpy as np

data = open('Dec_6/input.txt','r').read().strip().split('\n')

split_data = [list(line) for line in data]

current_loc = [0,0]
current_dir = 'up'
safety = 0
final_count = 0

for i, row in enumerate(split_data):
    for j, x in enumerate(row):
        if x in ['v','<','>','^']:
            print(x)
            current_loc = [i,j]
            match x:
                case 'v':
                    current_dir = 'down'
                case '<':
                    current_dir = 'left'
                case '>':
                    current_dir = 'right'
                case '^':
                    current_dir = 'up'

def turn_right():
    global current_dir
    print(f'Starting dir: {current_dir}')
    dirs = ['up','right','down','left'] # each is 90 deg right of the last
    if current_dir == 'left':
        current_dir = 'up'
    elif current_dir in dirs:
        current_dir = dirs[dirs.index(current_dir)+1]
    else:
        print('Turn right from WHAT? ({current_dir})')


# def check(dir,loc):
#     print('Checking')
#     temp_loc = [0,0]
#     # return '#' if a # is spotted. return True if not # and in-bounds. return False if out of bounds.
#     match dir:
#         case 'up':
#             temp_loc = [loc[0]-1,loc[1]]
#         case 'down':
#             temp_loc = [loc[0]+1,loc[1]]
#         case 'left':
#             temp_loc = [loc[0],loc[1]-1]
#         case 'right':
#             temp_loc = [loc[0],loc[1]+1]
    
#     try:
#         target_dest = split_data[temp_loc[0]][temp_loc[1]]
#         if target_dest == '#':
#             return '#'
#         else:
#             return True
#     except:
#         return False

def check(dir, loc):
    temp_loc = [loc[0], loc[1]]
    # Adjust temp_loc based on direction
    match dir:
        case 'up':
            temp_loc[0] -= 1
        case 'down':
            temp_loc[0] += 1
        case 'left':
            temp_loc[1] -= 1
        case 'right':
            temp_loc[1] += 1

    # Check if out of bounds
    if temp_loc[0] < 0 or temp_loc[0] >= len(split_data) or temp_loc[1] < 0 or temp_loc[1] >= len(split_data[0]):
        return False  # Out of bounds

    target_dest = split_data[temp_loc[0]][temp_loc[1]]
    if target_dest == '#':
        return '#'  # Obstacle
    else:
        return True  # Valid position


def traverse(dir,loc):
    global final_count
    check_dir = check(dir,loc)
    print(check_dir)
    print(f'Traversing {dir} from {loc}')
    match check_dir:
        case '#':
            turn_right()
            print(f'---=== New dir: {current_dir} ===---')
        case 0:
            print(f'Location {loc} is out of bounds. Is it over?')
            return 'End'
        case 1:
            temp_loc = loc
            match dir:
                case 'left':
                    current_loc[1] -= 1
                case 'right':
                    current_loc[1] += 1
                case 'up':
                    current_loc[0] -= 1
                case 'down':
                    current_loc[0] += 1
            split_data[temp_loc[0]][temp_loc[1]] = 'X'
            final_count += 1
    print(f'New loc: {current_loc}')

safety_limit = 15000

if __name__ == '__main__':
    while True:
        safety += 1
        if safety > safety_limit:
            break
        traversal = traverse(current_dir,current_loc)
        if traversal == 'End':
            for line in split_data:
                print(''.join(line))
            break
    with open('output.txt','w') as file:
        for item in split_data:
            for char in item:
                file.write(char)
            file.write('\n')
    #print(split_data)
    print(final_count)