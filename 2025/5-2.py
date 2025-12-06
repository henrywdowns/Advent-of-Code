from core import AOCD
puzzle = AOCD(5)
data = {
    "ranges":[x for x in puzzle.get_list('\n\n')[0].split('\n')],
    "ids": [x for x in puzzle.get_list('\n\n')[1].split('\n')]
    }
intervals = [[int(x.split('-')[0]),int(x.split('-')[1])] for x in data['ranges']]
intervals = sorted(intervals, key=lambda x: x[0])
merged = []
for start, end in intervals:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start,end])
    else:
        merged[-1][1] = max(merged[-1][1],end)
running_total = 0
for start, end in merged:
    running_total += end-start+1
puzzle.submit_answer(running_total)