with open("C:\Programming\Advent of Code2020\Day Four\Day4 Input.txt", "r") as f:
	#input = f.readlines()
    #input = [passport for passport in f.read().split('\n\n')]
    input = [line.strip() for line in f]
    
    
REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid, passports, passport = 0, [], {}    

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
        valid += 1
    
	
print(valid)