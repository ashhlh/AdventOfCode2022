# part 2

array = []
score = 0
with open("02/data.txt") as f:
    for line in f:
        array.append(line.strip())

for x in array:
    currentSet = x.split(" ")
    if currentSet[0] == "A": #first move = Rock
        if currentSet[1] == "X": #need to lose
            score += 3 #pick scissors
            score += 0 #lose
        elif currentSet[1] == "Y": #need to draw
            score += 1 #pick rock
            score += 3 #draw
        elif currentSet[1] == "Z": #need to win
            score += 2 #pick paper
            score += 6 #win
    elif currentSet[0] == "B": #first move = Paper
        if currentSet[1] == "X": #need to lose
            score += 1 #pick rock
            score += 0 #lose
        elif currentSet[1] == "Y": #need to draw
            score += 2 #pick paper
            score += 3 #draw
        elif currentSet[1] == "Z": #need to win
            score += 3 #pick scissors
            score += 6 #win
    elif currentSet[0] == "C": #first move = Scissors
        if currentSet[1] == "X": #need to lose
            score += 2 #pick paper
            score += 0 #lose
        elif currentSet[1] == "Y": #need to draw
            score += 3 #pick scissors
            score += 3 #draw
        elif currentSet[1] == "Z": #need to win
            score += 1 #pick rock
            score += 6 #win
print(score)        
    