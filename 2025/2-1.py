from aocd_api import AOCD


puzzle = AOCD(2,2025)

data = puzzle.get_list(',')

invalid_sum = 0

for i in data:
    # split the first and last
    split = i.split('-')
    first = int(split[0])
    # these are inclusive ranges so need to add 1 to last
    last = int(split[1])+1
    ids = [x for x in range(first,last)]
    for id in ids:
        str_id = str(id)
        if len(str_id)%2 == 0:
            midpoint = int(len(str_id)/2)
            if str_id[:midpoint] == str_id[midpoint:]:
                invalid_sum += int(id)


puzzle.submit_answer(invalid_sum)