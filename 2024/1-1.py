from core import AOCD
import re, numpy as np

puzzle = AOCD(1,2024)
data = puzzle.data

data = [(re.split(' +',line)) for line in data.split('\n')]
for x in range(len(data)):
    for y in range(len(x)):
        data[x][y] = str(y)
data = np.transpose(data)

print(data)