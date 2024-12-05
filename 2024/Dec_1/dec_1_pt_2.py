data = open('Dec_1/pt_1_input.txt','r').read().strip()

data_str = str(data)
data_arr = data_str.split()

ans_total = 0

left_list = []
right_list = []

for i, item in enumerate(data_arr):
    if i % 2 == 0:
        left_list.append(item)
    else:
        right_list.append(item)

for left_id in left_list:
    left_id_count = 0
    for right_id in right_list:
        if right_id == left_id:
            left_id_count += 1
    ans_total += (int(left_id) * left_id_count)

print(ans_total)