array = []

with open("03/data.txt", "r") as file:
    for line in file:
        stripped = line.strip()
        array.append(stripped)

def getLength(string):
    return len(string)

def split(string):
    string1 = string[0:getLength(string)//2]
    string2 = string[getLength(string)//2:]
    return string1, string2

def charCompare(): 
    return

for x in array:
    split(x)
    print(set(split(x)))
