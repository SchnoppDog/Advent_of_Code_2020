def task1():
    tasks       = []
    idCounter   = 0
    taskslen    = 0
    taskCounter = 0
    acc         = 0
    loopCounter = {}

    with open("files_for_days/day8.txt", "r") as file:
        for line in file:
            line = line.rstrip()
            line = line.split()
            line.append(idCounter)
            tasks.append(line)
            idCounter += 1
    
    taskslen = len(tasks)
    while True:
        # Before Change: 1866 -> Too High
        # Atfer Change:
        operation       = tasks[taskCounter][0]
        operationValue  = tasks[taskCounter][1]
        operationId     = tasks[taskCounter][2]
        # -> 3532 -> Too High

        if taskCounter == taskslen:
            taskCounter = 0

        if operationId in loopCounter.keys():
            if loopCounter[operationId] == 2:
                print("Acc-Value before loop: ", acc)
                break

        # if tasks[taskCounter][2] == 0:
        #     loopCounter += 1

        #     if loopCounter == 2:
        #         print("Acc-Value before loop: ", acc)
        #         break

        if operation == "acc":
            acc = acc + int(operationValue)
            if operationId not in loopCounter.keys():
                loopCounter[operationId] = 1

            else:
                loopCounter[operationId] = loopCounter[operationId] + 1
            
            taskCounter += 1
        
        if operation == "jmp":
            taskCounter = taskCounter + int(operationValue)
            if operationId not in loopCounter.keys():
                loopCounter[operationId] = 1

            else:
                loopCounter[operationId] = loopCounter[operationId] + 1

        if operation == "nop":
            if operationId not in loopCounter.keys():
                loopCounter[operationId] = 1

            else:
                loopCounter[operationId] = loopCounter[operationId] + 1
            
            taskCounter += 1

task1()