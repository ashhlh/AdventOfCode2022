# Part 2

array = []

with open("01/data.txt") as f: # Open the file
    for line in f: # For each line in the file
        line = line.replace("\n", "") # Remove the newline character
        array.append(line) # Add the line to the array

count = 0
maxValue = []

for x in array:
    if x == '':
        maxValue.append(count)
        count = 0
    elif x != None:    
        count = count + int(x)
sortedMax = sorted((maxValue), reverse=True)
top3 = sortedMax[0] + sortedMax[1] + sortedMax[2]
print("Top 3: " + str(top3))


