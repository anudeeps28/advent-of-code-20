with open ('day3p1_input.txt') as f:
    lines = f.readlines()
map = [str(line.strip()) for line in lines]

def tree(down,right):
    tree = 0
    row, col = 0,0

    while row+1 < len(map):
        row += right
        col += down

        space = map[row][col % len(map[row])]
        if space == "#":
            tree += 1

    return(tree)

t1 = (tree(1,1))
t2 = (tree(3,1))
t3 = (tree(5,1))
t4 =  (tree(7,1))
t5 = (tree(1,2))

product = t1*t2*t3*t4*t5
print(product)
