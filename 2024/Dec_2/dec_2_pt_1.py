data = str(open('Dec_2/input.txt','r').read().strip())
data = data.split('\n')
data = [list(map(int, level.split(' '))) for level in data]

count = 0

for row in data:
    interval_check = all(1 <= abs(row[i+1]-row[i]) <= 3 for i in range(len(row)-1))
    if interval_check and ((row == sorted(row)) or (row == sorted(row,reverse=True))):
        count +=1

print(count)