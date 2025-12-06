from functools import reduce
from aocd_api import AOCD
import re
import numpy as np

puzzle = AOCD(6)
data = puzzle.data
data = data.split('\n')
for idx,item in enumerate(data):
    data[idx] = re.split(" +",data[idx].strip())

data = np.transpose(data).tolist()
results = []
for p_idx, prob in enumerate(data):
    match prob.pop(-1):
        case '*':
            results.append(reduce(lambda x,y: int(x)*int(y),prob))
        case '+':
            results.append(reduce(lambda x,y: int(x)+int(y),prob))
        case _:
            print(prob)
            raise ValueError
results = reduce(lambda x,y: x + y,results)
puzzle.submit_answer(results)