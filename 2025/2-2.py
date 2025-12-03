from aocd_api import AOCD
import math

puzzle = AOCD(2,2025)

data = puzzle.get_list(',')

for i in data[4:5]:
    print(i)
    # split the first and last
    split = i.split('-')
    first = int(split[0])
    # these are inclusive ranges so need to add 1 to last
    last = int(split[1])+1
    ids = [x for x in range(first,last)]
    for id in ids:
        midpoint = math.floor(int(len(str(id))/2))
        print(f'len: {len(str(id))} -- midpoint: {midpoint}')