with open ('day3p1_input.txt') as f:
    lines = f.readlines()
map = [str(line.strip()) for line in lines]

tree = 0
row, col = 0,0

while row+1 < len(map):
    row += 1
    col += 3

    space = map[row][col % len(map[row])]
    if space == "#":
        tree += 1

print (tree)
