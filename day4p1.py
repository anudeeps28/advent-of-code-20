with open ('day4p1_input.txt') as f:
    lines = f.readlines()

input = [str(line.strip()) for line in lines]
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def is_valid_passport(pp):
    for field in fields:
        if field not in pp:
            return False
    return True

validCount = 0

currentPassport = ''
for line in input:
    if line != '':
        currentPassport += '' + line
    else:
        if is_valid_passport(currentPassport):
            validCount += 1
        currentPassport = ''

if is_valid_passport(currentPassport):
    validCount += 1

print(validCount)
