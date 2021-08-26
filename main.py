import json

while True:
    file = input("Enter the filename\n")
    print("\nOpening " + file + '...\n')
    try:
        f = open(file,'r',encoding='ISO-8859-1')
        break
    except IOError:
        input("Error in file opening, please type correct filename\n")

lineDict = {}

for line in f:
    splitted = line.split()
    for word in splitted:
        if '.php:' in word:
            # print(word)
            combo = word.split(":")
            # print(combo)
            lineNum = combo[1]
            fileName = combo[0]
            lineDict[lineNum] = fileName

with open('lineDict.txt', 'w') as file:
    file.write(json.dumps(lineDict))

print('Finished')

f.close()