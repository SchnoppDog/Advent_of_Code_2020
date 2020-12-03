# steps               = 3
# stepsMoved          = steps
r1d1                = True
r3d1                = False
r5d1                = False
r7d1                = False
rxd1Steps           = [1, 3, 5, 7]
# r1d1Steps           = 1
# r3d1Steps           = 3
# r5d1Steps           = 5
# r7d1Steps           = 7
stepsMoves          = 0
skipFirstLine       = False
treeCounter         = 0
openSpaceCounter    = 0
charRepition        = 1
charRepitionTimes   = 1
openSpace           = "."
tree                = "#"
slopes              = {
    
}

lines = 2

# "R1D1": {
#         "Trees": 0,
#         "Open Space": 0,
#     },
#     "R3D1": {
#         "Trees": 0,
#         "Open Space": 0,
#     },
#     "R5D1": {
#         "Trees": 0,
#         "Open Space": 0,
#     },
#     "R7D1": {
#         "Trees": 0,
#         "Open Space": 0,
#     },
#     "R1D2": {
#         "Trees": 0,
#         "Open Space": 0,
#     }

for steps in rxd1Steps:
    stepsMoved = steps
    print(stepsMoved)

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
                    print("\n\tLines: ", lines)
                    print(stepsMoved)
                    lines +=1
                    stepsMoved += steps
                
                else:
                    skipFirstLine = True

        slopes[f"R{steps}D1"]               = {}
        slopes[f"R{steps}D1"]["Trees"]      = treeCounter
        slopes[f"R{steps}D1"]["Open Space"] = openSpaceCounter
        treeCounter                         = 0
        openSpaceCounter                    = 0
        lines = 0

# print("Trees: ", treeCounter)
# print("Open Space: ", openSpaceCounter)
print(slopes)