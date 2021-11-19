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

for passport in input:
    row = get_row(passport[:7])
    col = get_col(passport[7:])

    id = row * 8 + col


    if id > largest:
        largest = id

print(largest)
