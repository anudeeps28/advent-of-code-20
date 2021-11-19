with open ('day5_input.txt') as f:
    lines = f.readlines()

input = [str(line.strip()) for line in lines]
largest = 0

def get_row(passport):
    lower = 0
    higher = 127

    for i in range(6): #i takes values 0 through 6 one by one
        half = (higher + lower) // 2
        if passport[i] == "F":
            higher = half
        elif passport[i] == "B":
            lower = half + 1

    if passport[6] == "F":
        return lower
    else:
        return higher


def get_col(passport):
    lower = 0
    higher = 7

    for i in range(2):
        half = (higher + lower) // 2
        if passport[i] == "L":
            higher = half
        elif passport[i] == "R":
            lower = half + 1

    if passport[2] == "L":
        return lower
    else:
        return higher
rrow = []
rcol = []
rid = []
for passport in input:
    row = get_row(passport[:7])
    rrow.append(row)
    col = get_col(passport[7:])
    rcol.append(rcol)
    id = row * 8 + col
    rid.append(id)

prev = 0
missing = []
# print (rid)
for i in sorted(rid):
    if prev != i-1:
        missing.append(i-1)
    prev = i

print(missing)
# print (sorted(rid))
