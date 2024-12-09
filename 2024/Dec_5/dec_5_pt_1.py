import numpy as np
data = open('Dec_5/input.txt','r').read().strip().split('\n\n')


rules_temp = data[0].split('\n')
rules = []
for line in rules_temp:
    rules.append(line.split('|'))
order_temp = data[1].split('\n')
orders = []
for item in order_temp:
     split_item = item.split(',')
     orders.append(split_item)
print(f'Orders: {orders}')

total = 0

def get_middle(row):
        row_ints = row
        if type(row) != list:
            row_ints = row.split(',')
        middle = row_ints[int(len(row_ints)/2)]
        return int(middle)

def elim_orders():
    elim = orders
    print(f'Len: {len(elim)}')
    for rule in rules:
        for order in orders:
            if rule[0] in order and rule[1] in order:
                try:
                    rule_0 = order.index(rule[0])
                    rule_1 = order.index(rule[1])
                    test_rule = rule_0 < rule_1
                    if test_rule:
                        pass
                    else:
                        print(f'Breaks rule - removing\nRule: {rule}\nOrder:{order}')
                        elim.remove(order)
                except:
                    print('Error - couldn\'t get indices')
            else:
                pass
    print(f'After: {len(elim)}')
    return elim

def get_middle(some_array):
    total = 0
    for item in some_array:
        middle_index = len(item)//2
        middle_number = int(item[middle_index])
        total += middle_number
    return total

print(get_middle(elim_orders()))

print(f'Total: {total}')