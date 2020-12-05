def task1():
    lines = []
    with open("files_for_days/day4.txt", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            lines.append(line.replace("\r", ""))        # Example-Output: ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", 
                                                        # "byr:1937 iyr:2017 cid:147 hgt:183cm", ""]
    
    passports = []
    for line in lines:
        lineContents = line.split(" ")
        for lineContent in lineContents:
            passports.append(lineContent)       # Example-Output: ["ecl:gry", "pid:860033327", "eyr:2020", "hcl:#fffffd" ..., "", ...]
    
    passportObj         = {}
    passportCounter     = 1
    passportObj[f"passport_{passportCounter}"] = {}
    for passportEntry in passports:
        if len(passportEntry) == 0:
            passportCounter += 1
            passportObj[f"passport_{passportCounter}"] = {}
            continue
        
        entryId     = passportEntry.split(":")[0]
        entryValue  = passportEntry.split(":")[1]
        # Example-Output: passportObj = {"passport_1": {"ecl": "gry", "pid": "860033327", "eyr": "2020" ...}, "passport_2": {...}}
        passportObj[f"passport_{passportCounter}"][entryId] = entryValue

    # Looping through nested dictionary
    validPassports = 0
    for nestedPassport in passportObj.keys():
        # nestedPassport = passport_1, passport_2 etc.
        passportKeys = 0
        for passport in passportObj[nestedPassport].keys():
            # passport = keys of passportObj with passport_1, passport_2 etc.
            if passport == "cid":
                # Ignoring CID-Field
                passportKeys -= 1  
            passportKeys += 1
        
        if passportKeys >= 7:
            validPassports += 1
    
    print("Valid Passports: ", validPassports)

# def validatePassport(passportObj):

task1()

# Main Concept:

# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in

# 1. Remove any \n\r and push it into an array
# 2. Make a full String of every data e.g: ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm
# 3. Make a information-pattern and check each string if it contains every information
# 4. Push valid Data into a dictionary
# 5. Return the dictionary