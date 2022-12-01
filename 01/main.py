# Part 1

array = []

with open("01/data.txt") as f: # Open the file
    for line in f: # For each line in the file
        line = line.replace("\n", "") # Remove the newline character
        array.append(line) # Add the line to the array

count = 0
maxValue = 0

for x in array:
    if x == '':
        if count > maxValue:
            maxValue = count
        count = 0
    elif x != None:    
        count = count + int(x)
print("Max value: " + str(maxValue))

