from functools import reduce
from core import AOCD
import re
import numpy as np

puzzle = AOCD(6)
data = puzzle.data

data = data.split('\n')
data = [list(reversed(list(line))) for line in data]
data = np.transpose(data).tolist()
gt = 0
equation = []
for line in data:
    accum = ''
    for char in line:
        if char.isnumeric():
            accum += char
        elif char == '+' or char == '*':
            equation.append(int(accum))
            tot = reduce(lambda x, y: x + y if char == '+' else x * y, equation)
            gt += tot
            accum = ''
            equation = []
            continue
    if accum:
        equation.append(int(accum))
    accum = ''
# puzzle.submit_answer(gt)