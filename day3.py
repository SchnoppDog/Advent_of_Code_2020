tree                = "#"
openSpace           = "."
steps               = 3
stepsMoved          = steps
skipFirstLine       = False
treeCounter         = 0
openSpaceCounter    = 0
charRepition        = 1
charRepitionTimes   = 1



with open("files_for_days/day3.txt", "r") as file:
    # pattern = []
    # pattern.append(file.readline().replace("\n", ""))
    # pattern.append(file.readline().replace("\n", ""))
    # pattern.append(file.readline().replace("\n", ""))
    # pattern.append(file.readline().replace("\n", ""))
    # print(pattern)

    # for characters in pattern:
    #     if skipFirstLine == True:
    #         if len(characters) > steps:
    #             print(characters)
    #             print(stepsMoved)
    #             print(characters[stepsMoved])
    #             if characters[stepsMoved] == tree:
    #                 treeCounter += 1

    #             else:
    #                  openSpaceCounter += 1

    #         stepsMoved += steps

    #         # else:
    #         #     characterString = 
    #     else:
    #         print(characters)
    #         skipFirstLine = True
        
    for line in file:
        pattern = []
        pattern.append(line.split())

        for characters in pattern:
            if skipFirstLine == True:
                characterString = characters[0] * charRepitionTimes
                

                if stepsMoved / len(characterString) >= charRepition:
                    charRepitionTimes += 1
                    characterString = characters * charRepitionTimes
                
                else:
                    if characterString[stepsMoved] == "#":
                        treeCounter += 1

                    else:
                        openSpaceCounter += 1

                    print(len(characterString))
                    print(stepsMoved)
                    print(characterString[stepsMoved])
                    stepsMoved += steps
            
            else:
                skipFirstLine = True

print("Trees: ", treeCounter)
print("Open Space: ", openSpaceCounter)