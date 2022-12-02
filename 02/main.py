# part 1

array = []
score = 0
with open("02/data.txt") as f:
    for line in f:
        array.append(line.strip())

for x in array:
    currentSet = x.split(" ")
    if currentSet[0] == "A": #first move = Rock
        if currentSet[1] == "X": #second move = Rock
            score += 1
            score += 3
        elif currentSet[1] == "Y": #second move = Paper
            score += 2
            score += 6
        elif currentSet[1] == "Z": #second move = Scissors
            score += 3
            score += 0
    elif currentSet[0] == "B": #first move = Paper
        if currentSet[1] == "X": #second move = Rock
            score += 1
            score += 0
        elif currentSet[1] == "Y": #second move = Paper
            score += 2
            score += 3
        elif currentSet[1] == "Z": #second move = Scissors
            score += 3
            score += 6
    elif currentSet[0] == "C": #first move = Scissors
        if currentSet[1] == "X": #second move = Rock
            score += 1
            score += 6
        elif currentSet[1] == "Y": #second move = Paper
            score += 2
            score += 0
        elif currentSet[1] == "Z": #second move = Scissors
            score += 3
            score += 3
print(score)        
    