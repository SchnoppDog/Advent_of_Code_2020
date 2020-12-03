tree                = "#"
openSpace           = "."
steps               = 3
stepsMoved          = steps
skipFirstLine       = False
treeCounter         = 0
openSpaceCounter    = 0
charRepition        = 1
charRepitionTimes   = 1
lines               = 0



with open("files_for_days/day3.txt", "r") as file:
    for line in file:
        pattern = []
        pattern.append(line.split())
        lines += 1

        for characters in pattern:
            if skipFirstLine == True:
                characterString = characters[0] * charRepitionTimes

                if stepsMoved / len(characterString) >= charRepition:
                    charRepitionTimes += 1
                    characterString = characters[0] * charRepitionTimes
                
                if characterString[stepsMoved] == "#":
                    treeCounter += 1

                else:
                    openSpaceCounter += 1

                stepsMoved += steps
            
            else:
                skipFirstLine = True

print("Trees: ", treeCounter)
print("Open Space: ", openSpaceCounter)