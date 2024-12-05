data = str(open('2024/Dec_2/input.txt','r').read().strip())

# all items in row must increase or decrease
# adjacent levels must differ by >= 1 and <= 3
data = data.split('\n')
count = 0
limit = 0
limit_cap = 10
for row in data:
    if limit < limit_cap:
        print(f'limit: {limit}')
        print(row)
    split_row = row.split(' ')
    sorted_row = sorted(split_row)
    if limit < limit_cap:
        print(split_row)
    if not (split_row == sorted_row):
        if limit < limit_cap:
            print("not sorted fwd")
        sorted_row = sorted(sorted_row,reverse=True)
        if not (split_row == sorted_row):
            if limit < limit_cap:
                print("not sorted bkwd\nnext")
            limit += 1
            continue
    if limit < limit_cap:
        print("sorted")
    within_range = all([1 <= (int(split_row[i+1])-int(split_row[i])) <= 3 for i in range(len(split_row)-1)])
    if limit < limit_cap:
        print(within_range)
    if within_range:
        if limit < limit_cap:
            print("range checks out")
        count += 1
    else:
        if limit < limit_cap:
            print("range doesn't check out")
    limit += 1
print(count)