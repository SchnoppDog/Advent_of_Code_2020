def task1():
    groups          = []
    nestedGroups    = []
    lines           = []
    groupYesCounts  = []
    countaddGroups  = 0
    yesSum          = 0

    with open("files_for_days/day6.txt", "r") as file:
        for line in file:
            line = line.rstrip()
            lines.append(line)
    
    for string in lines:
        if string == "":
            groups.append(nestedGroups)
            nestedGroups = []
            countaddGroups += 1
            continue
        
        else:
            nestedGroups.append(string)
            if countaddGroups == len(lines) - 1:
                groups.append(nestedGroups)
        
        countaddGroups += 1

    for group in groups:
        # Task 1:
        groupAnswers    = group[0]
        # Task 2:
        groupAnswersLen = len(group[0])
        if len(group) == 1:
            # Task 1:
            groupYesCounts.append(len(group[0]))
            continue

        for answer in group:
            for letter in answer:
                # Task 1:
                # if letter not in groupAnswers:
                #     groupAnswers = groupAnswers + letter
                # Task 2:
                if letter not in groupAnswers:
                    groupAnswersLen -= 1

        # Task 1:
        # groupYesCounts.append(len(groupAnswers))
        # Task 2:
        if groupAnswersLen <= 0:
            groupAnswersLen = 0

            # Idea Task2: -> Match the answers after the first one with the first one and make a new String which contains all letter everyone crossed with a yes

        groupYesCounts.append(groupAnswersLen)
    
    for yesCounts in groupYesCounts:
        yesSum += yesCounts
    
    print("Sum of Yes-Answers: ", yesSum)
    

task1()