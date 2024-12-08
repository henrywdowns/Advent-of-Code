import re

data = str(open('Dec_3/input.txt','r').read().strip())

found = re.findall(r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)",data)
total = int(0)
do_dummy = 1

for x,y,do,dont in found:
    if do:
        do_dummy = 1
    elif dont:
        do_dummy = 0
    else:
        total += int(x)*int(y)*do_dummy

print(total)