# Note: This is quite a horrific code and can be written A LOT BETTER. But for general comprehension it's ok.
# Will be updated in the future (I guess ...)

rxd1Steps           = [1, 3, 5, 7]
r1d2Steps           = 2
r1d2                = False
skipFirstLine       = False
treeCounter         = 0
openSpaceCounter    = 0
charRepition        = 1
charRepitionTimes   = 1
lineNumber          = 1
treeSum             = 1
openSpaceSum        = 1
openSpace           = "."
tree                = "#"
slopes              = {}

# Task 1 and first half of 2
for steps in rxd1Steps:
    stepsMoved = steps

    with open("files_for_days/day3.txt", "r") as file:
            
        for line in file:
            pattern = []
            pattern.append(line.split())

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

        slopes[f"R{steps}D1"]               = {}
        slopes[f"R{steps}D1"]["Trees"]      = treeCounter
        slopes[f"R{steps}D1"]["Open Space"] = openSpaceCounter
        treeCounter                         = 0
        openSpaceCounter                    = 0
        skipFirstLine                       = False

print(slopes)

# Task 2 second half
skipFirstLine       = False
treeCounter         = 0
openSpaceCounter    = 0
lineNumber          = 1
charRepitionTimes   = 1
steps               = 1
stepsMoved          = steps

with open("files_for_days/day3.txt", "r") as file:
            
    for line in file:
        pattern = []
        pattern.append(line.split())

        for characters in pattern:
            if skipFirstLine == True:
                if lineNumber % 2 == 1:
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

            lineNumber += 1

print(treeCounter)
print(openSpaceCounter)