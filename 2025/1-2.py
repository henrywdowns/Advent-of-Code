from aocd_api import AOCD

puzzle = AOCD(1,2025)

data = [line for line in puzzle.data.split('\n') if line]

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
# iterate through data
for x in data:
    # grab the number part for easy access
    x_value = int(x[1:])
    test += 1
    if test < 15: print(f'base: {base} -- x: {x}')
    # account for turns larger than one full turn:
    if int(x[1:]) > 100:
        # print(f'old, big x: {x} -- floor: {x_value//100}')
        # floor divide by 100 (ie 409 -> 4) and add the number of full turns directly
        zero_count += x_value//100
        # set base equal to the modulo (remainder) and proceed with the leftover part of the turn
        x = x[0]+str(x_value%100)
        # print(f'new x: {x}')
    base = turn(base,x)
    if test < 15: print(f'New base: {base}')
    # if we land on or past "0" (0 for L, 100 for R) then take note
    if base <= 0 or base >= 100:
        zero_count += 1
        if test < 15:
            print('zero!')
    # set base equal to remainder for next iter
    base = base%100
print(zero_count)

# puzzle.submit_answer(zero_count)