# def task1():
#     with open("files_for_days/examples/day4.txt", "r") as file:


# print(task1())

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