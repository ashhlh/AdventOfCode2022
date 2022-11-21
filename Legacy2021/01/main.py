array = []
increaseCount = 0
currentNum = 0
previousNum = 0

for line in open('Legacy2021/01/input.txt', 'r'):
    array.append(line)

for x in array:
    currentNum = x
    if previousNum == 0:
        pass
    elif currentNum > previousNum:
        increaseCount = increaseCount + 1
        print (x + " increase!")
    else:
        print (x + " decrease!")
    previousNum = currentNum

print(increaseCount)
# increaseCount is 1 off?



