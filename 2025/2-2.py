from core import AOCD

puzzle = AOCD(2,2025)

data = puzzle.get_list(',')

test_data = ['11-22','95-115','998-1012','1188511880-1188511890','222220-222224',
'1698522-1698528','446443-446449','38593856-38593862','565653-565659',
'824824821-824824827','2121212118-2121212124']

# use split_equal() and factors() and see if any of the outputs are lists of identical values
def compare_chunks(sequence):
    sequence = str(sequence)
    fs = factors(len(sequence))
    for f in fs:
        chunks = split_equal(sequence,f)
        if all([x == chunks[0] for x in chunks]):
            return True
    return False
# take a number and split s into equal chunks
def split_equal(s, size):
    return [s[i:i+size] for i in range(0, len(s), size)]

# get all the factors that don't equal n, which i can use with split_equal()
def factors(n):
    fs = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            fs.append(i)
            if i != n // i:
                fs.append(n // i)
        i += 1
    fs = sorted(fs,reverse=True)[1:]
    return fs

running_total = 0

for i in data:
    print(i)
    # split the first and last
    split = i.split('-')
    first = int(split[0])
    # these are inclusive ranges so need to add 1 to last
    last = int(split[1])+1
    ids = [x for x in range(first,last)]
    for id in ids:
        if compare_chunks(id):
            running_total += id

print(running_total)
# puzzle.submit_answer(running_total)