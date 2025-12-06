from core import AOCD

puzzle = AOCD(3)
data = puzzle.get_list('\n')

def optimize_line(line):
    result = ''
    line_arr = list(line) # break line into a list of chars
    def get_max(first_round=False):
        max_line = line_arr[:-1] if first_round else line_arr
        max_val = max(max_line) # get the largest integer in the list, excluding the last place if first_round (10s place cant be last)
        max_val_ind = line_arr.index(max_val) # get the index of the max int
        return int(max_val), max_val_ind
    val_1, val_ind_1 = get_max(first_round=True)
    line_arr = line_arr[(val_ind_1 + 1):] # adjust the list of chars to only be the items after val_1
    val_2, val_ind_2 = get_max()
    print(val_1, val_2, val_1 * 10 + val_2)
    return int((val_1 * 10) + val_2)

def do_the_thing():
    total = 0
    for line in data:
        line_value = optimize_line(line)
        total += line_value
    return total

# puzzle.submit_answer(do_the_thing())