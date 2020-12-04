passwordTimes           = []
passwordCharacter       = []
password                = []
validPasswords          = 0
invalidPasswords        = 0

with open("files_for_days/day2.txt", "r") as file:
    fileStripped    = []

    for line in file:
        fileStripped.append(line.split())       # Line Format: 4-5 r: rrrjr -> returns [["4-5", "r:", "rrrjr"], ...]


for charTimes in fileStripped:
    passwordTimes.append(charTimes[0].split("-"))       # charTimes Format: ["4-5", "r:", "rrrjr"] -> Returns [["4", "5"], ...]
    passwordCharacter.append(charTimes[1].replace(":", ""))         # Returns: ["r", ...]
    password.append(charTimes[2])       # Returns: ["rrrjr", ...]


# Part 1
# for counter in range(len(password)):
#     charCounter = 0
#     for char in password[counter]:
#         if char == passwordCharacter[counter]:
#             charCounter += 1
        
#     if charCounter >= int(passwordTimes[counter][0]) and charCounter <= int(passwordTimes[counter][1]):
#         print(counter)
#         validPasswords += 1

# Part 2
for counter in range(len(password)):
    # if (position x of(password) == charToEqual and position y of(password) != charToEqual) and -> Other way around
    if (password[counter][int(passwordTimes[counter][0]) - 1] == passwordCharacter[counter] and password[counter][int(passwordTimes[counter][1]) - 1] != passwordCharacter[counter]) or (password[counter][int(passwordTimes[counter][0]) - 1] != passwordCharacter[counter] and password[counter][int(passwordTimes[counter][1]) - 1] == passwordCharacter[counter]):
        validPasswords += 1
    
    else:
        invalidPasswords += 1

print(validPasswords)
print(invalidPasswords)

