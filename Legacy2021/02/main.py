array = []
horizontal = 0
depth = 0

for line in open('Legacy2021/02/input.txt', 'r'):
    array.append(line)
for movement in array:

    splitString = movement.split(" ")
    direction = splitString[0]
    distance = splitString[1]

    if direction == 'forward':
        horizontal = horizontal + int(distance)
    if direction == 'up':
        depth = depth - int(distance)
    if direction == 'down':
        depth = depth + int(distance)



print("horizontal = " + str(horizontal))
print("depth = " + str(depth))
print("multiplied = " + str(depth * horizontal))

