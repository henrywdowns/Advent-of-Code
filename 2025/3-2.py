from aocd_api import AOCD

puzzle = AOCD(3)
data = puzzle.get_list('\n')

def optimize_line(line):
    count = 0
    result = ''
    result_idxs = []
    line_arr = list(line) # break line into a list of chars
    def get_max():
        nonlocal count, result, result_idxs, line
        count += 1
        last_round = True if count == 12 else False 
        max_line = line_arr[:-(12-count)] if not last_round else line_arr
        max_val = max(max_line) # get the largest integer in the list, excluding the last place if first_round (10s place cant be last)
        max_val_ind = line_arr.index(max_val) # get the index of the max int
        result += str(max_val)
        result_idxs.append(max_val_ind)
        return int(max_val), max_val_ind
    val_1, val_ind_1 = get_max() # first round is a special case but 2-12 can work iteratively
    while len(result) < 12:
        line_arr = line_arr[(result_idxs[-1]+1):] # adjust the list of chars to only be the items after the most recent max_val_ind
        val_x, val_ind_x = get_max()
    return int(result)

def do_the_thing():
    total = 0
    for line in data:
        line_value = optimize_line(line)
        total += line_value
    return total

final_result = do_the_thing()

puzzle.submit_answer(do_the_thing())