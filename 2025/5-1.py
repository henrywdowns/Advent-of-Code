from core import AOCD

puzzle = AOCD(5)
data = puzzle.data
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
        merged[-1][1] = max(merged[-1][1], end)
final_count = 0
for x in data['ids']:
    if any(interval[0] <= int(x) <= interval[1] for interval in merged):
        final_count += 1

print(final_count)
# puzzle.submit(final_count)