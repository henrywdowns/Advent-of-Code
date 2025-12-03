from aocd_api import AOCD

puzzle = AOCD(1,2025)

data = puzzle.get_list('\n')

def turn(current_pos,value):
    dir = value[0].upper()
    if dir not in ['L','R']:
        raise ValueError
    num = int(value[1:])
    if dir == 'L':
        return current_pos - num
    else:
        return current_pos + num
    
base = 50
zero_count = 0
test = 0

for x in data:
    x_value = int(x[1:])
    test += 1
    if test < 15: print(f'base: {base} -- x: {x}')
    if int(x[1:]) > 100:
        zero_count += x_value//100
        x = x[0]+str(x_value%100)
    if base == 0 and x[0] == 'L':
        zero_count -= 1
    base = turn(base,x)
    if test < 15: print(f'New base: {base}')
    if base <= 0 or base >= 100:
        zero_count += 1
        if test < 15:
            print(f'zero! count: {zero_count}')
    base = base%100
print(zero_count)

puzzle.submit_answer(zero_count)