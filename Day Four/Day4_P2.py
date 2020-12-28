import re

with open("C:\Programming\Advent of Code2020\Day Four\Day4 Input.txt", "r") as f:
	#input = f.readlines()
    #input = [passport for passport in f.read().split('\n\n')]
    input = [line.strip() for line in f]
    
    
REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eyecolor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valid, passports, valid_passports, passport = 0, [], [], {}    

input.append('')

for line in input:
    if line == '':
        passports.append(passport)
        passport = {}
    else:
        data  = line.split()
        
        for field in data:
            field = field.split(":")
            passport[field[0]] = field[1]

for passport in passports:
    keys = passport.keys()
    if all(key in keys for key in REQUIRED_FIELDS):
        valid_passports.append(passport)
    

for passport in valid_passports:

    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False

    if len(passport.get("byr")) == 4 and 1920 <= int(passport.get("byr")) <= 2002:
        byr = True

    if len(passport.get("iyr")) == 4 and 2010 <= int(passport.get("iyr")) <= 2020:
        iyr = True

    if len(passport.get("eyr")) == 4 and 2020 <= int(passport.get("eyr")) <= 2030:
        eyr = True

    if passport.get("hgt").endswith("cm"):
        height = passport.get("hgt")[:-2]
        if 150 <= int(height) <= 193:
            hgt = True
    if passport.get("hgt").endswith("in"):
        height = passport.get("hgt")[:-2]
        if 59 <= int(height) <= 76:
            hgt = True

    if passport.get("hcl")[0] == '#' and len(passport.get("hcl")[1::]) == 6 and bool(re.match('^[abcdef0123456789]+$', passport.get("hcl")[1::])):
        hcl = True

    if passport.get("ecl") in eyecolor:
        ecl = True

    if len(passport.get("pid")) == 9 and passport.get("pid").isnumeric():
        pid = True

    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        valid += 1

print(valid)