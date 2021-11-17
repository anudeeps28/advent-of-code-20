with open ('day1_inputp1.txt') as f:
    lines = f.readlines()

nums = [int(line.strip()) for line in lines]

largest = -1
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        for k in range(i+2,len(nums)):
            num1 = nums[i]
            num2 = nums[j]
            num3 = nums[k]

            if num1 + num2 + num3 == 2020:
                balance = num1*num2*num3

                if balance > largest:
                    largest = balance

print (largest)
