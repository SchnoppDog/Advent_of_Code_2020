def task1():
    highestSeatId   = 0
    seatId          = []
    lines           = []
    fbValues        = []
    rlValues        = []

    with open("files_for_days/day5.txt", "r") as file:
        for line in file:
            lineLetter = line[7]
            line = line.replace("\n", "")
            line = line.split(line[7], 1)
            line[1] = lineLetter + line[1]
            lines.append(line)
        print(lines)

    for lineList in lines:
        upperHalfFB = 128
        upperHalfRL = 8
        lowerHalfFB = 0
        lowerHalfRL = 0
        lenFbList   = len(lineList[0]) - 1
        lenRlList   = len(lineList[1]) - 1

        for fbLetter in lineList[0]:
            if fbLetter == "F":
                upperHalfFB = ((upperHalfFB - lowerHalfFB) / 2) + lowerHalfFB
                # upperHalfBinary = upperHalf - 1

            elif fbLetter == "B":
                lowerHalfFB = ((upperHalfFB - lowerHalfFB) / 2) + lowerHalfFB

        if lineList[0][lenFbList] == "F":
            upperHalfBinaryFB = upperHalfFB - 1
            fbValues.append(upperHalfBinaryFB)

        elif lineList[0][lenFbList] == "B":
            fbValues.append(lowerHalfFB)

        for rlLetter in lineList[1]:
            if rlLetter == "R":
                lowerHalfRL = ((upperHalfRL - lowerHalfRL) / 2) + lowerHalfRL

            elif rlLetter == "L":
                upperHalfRL = ((upperHalfRL - lowerHalfRL) / 2) + lowerHalfRL
        
        if lineList[1][lenRlList] == "R":
            rlValues.append(lowerHalfRL)

        elif lineList[1][lenRlList] == "L":
            upperHalfBinaryRL = upperHalfRL - 1
            rlValues.append(upperHalfBinaryRL)
    
    for counter in range(len(fbValues)):
        seatId.append(fbValues[counter] * 8 + rlValues[counter])
    
    for seatIds in seatId:
        if highestSeatId < seatIds:
            highestSeatId = seatIds

        else:
            highestSeatId = highestSeatId
        
        print("Seat-IDs: ", seatIds)

    print("Highest Seat-ID is: ", highestSeatId)
    # print(fbValues)
    # print(rlValues)
    # print(seatId)
    # print(highestSeatId)


task1()

# Task 2 will be missing since I don't understand the task and what I should do...