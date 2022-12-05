array = []
count = 0
with open("04/data2.txt") as f:
    for line in f:
        array.append(line.strip())

def getPair(x):
    split = x.split(",")
    return split

def awfulSplitting(x):
    set1value1=getPair(x)[0].split("-")[0]
    set1value2=getPair(x)[0].split("-")[1]
    set2value1=getPair(x)[1].split("-")[0]
    set2value2=getPair(x)[1].split("-")[1]
    return set1value1,set1value2,set2value1,set2value2

for x in array:
    if awfulSplitting(x)[0] >= awfulSplitting(x)[2] and awfulSplitting(x)[1] <= awfulSplitting(x)[3]:
        print(str(getPair(x)) + ".... set resides in other set")
        count += 1
    elif awfulSplitting(x)[2] >= awfulSplitting(x)[0] and awfulSplitting(x)[3] <= awfulSplitting(x)[1]:
        print(str(getPair(x)) + ".... set resides in other set")
        count += 1
    else:
        print(str(getPair(x)) + ".... set does not reside in other set")
        pass
print("count is " + str(count))



