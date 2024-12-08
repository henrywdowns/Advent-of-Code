import re

data = str(open('Dec_3/input.txt','r').read().strip())

found = re.findall(r'mul\((\d+),(\d+)\)',data)

total = 0

for tuple in found:
    total += int(tuple[0])*int(tuple[1])

print(total)