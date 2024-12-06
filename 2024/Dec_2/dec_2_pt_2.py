data = str(open('Dec_2/input.txt','r').read().strip())
data = data.split('\n')
data = [list(map(int, level.split(' '))) for level in data]

total = 0

def check_intervals(level):
        return all(1 <= abs(level[i+1]-level[i]) <= 3 for i in range(len(level)-1))

def check_safe(level):
    if check_intervals(level) and ((level == sorted(level)) or (level == sorted(level,reverse=True))):
        return 1
    else:
        for i in range(len(level)):
             temp_level = level[:i] + level[i+1:]
             if check_intervals(temp_level) and ((temp_level == sorted(temp_level)) or temp_level == sorted(temp_level,reverse=True)):
                  return 1    
    return 0
            
for level in data:
     total += check_safe(level)

print(total)

