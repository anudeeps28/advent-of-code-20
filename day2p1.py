with open ('day2p1_input.txt') as f:
    lines = f.readlines()

finalcount = 0
nums = [str(line.strip()) for line in lines]

for i in nums:
    first, password = i.split(":")
    lower,second2 = first.split("-")
    higher,letter = second2.split(" ")
    count = 0


    for i in password:
        if (i == letter):
            count += 1

    if (int(lower) <= count <= int(higher)):
        finalcount += 1

print(finalcount)
