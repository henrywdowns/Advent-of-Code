data = open('Dec_1/pt_1_input.txt','r').read().strip()

data_str = str(data)
data_arr = data_str.split()

left_list = []
right_list = []

for i, item in enumerate(data_arr):
    if i % 2 == 0:
        left_list.append(item)
    else:
        right_list.append(item)

left_list.sort()
right_list.sort()

ans = 0

for x in range(len(left_list)):
    ans += abs(int(left_list[x])-int(right_list[x]))

print(ans)