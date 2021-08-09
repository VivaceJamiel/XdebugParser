import json

while True:
    file = input("Enter the filename\n")
    print("\nOpening " + file + '...\n')
    try:
        f = open(file)
        break
    except IOError:
        input("Error in file opening, please type correct filename")

lineDict = {}

for line in f:
    splitted = line.split()
    for word in splitted:
        if '.php' in word:
            fileNameNum = word.split("/")
            final = fileNameNum[-1]
            combo = final.split(":")
            lineNum = combo[1]
            fileName = combo[0]
            lineDict[lineNum] = fileName

with open('lineDict.txt', 'w') as file:
    file.write(json.dumps(lineDict))


f.close()