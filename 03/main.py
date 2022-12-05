# part 1

array = []
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
total = 0
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

for string in array:
    string1 = string[0:getLength(string)//2]
    string2 = string[getLength(string)//2:]
    stringRange = range(0, getLength(string1))
    for x in stringRange:
        if string1[x] in string2:
            print(string1[x])
            total += numbers[letters.index(string1[x])]
            break

print(total)


