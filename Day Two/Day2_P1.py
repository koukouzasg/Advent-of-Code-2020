with open("C:\Programming\Advent of Code2020\Day Two\Day2 Input.txt") as f:
    input = f.readlines()

valid_passwords = 0    
  
for line in input:
    temp = line.split("-")
    minValue = int(temp[0])
    temp = temp[1].split()
    maxValue = int(temp[0])
    restriction = temp[1]
    restriction = restriction[0]
    password = temp[2]
    frequency = password.count(restriction)
    if  frequency >= minValue and frequency <= maxValue:
        valid_passwords += 1

print (valid_passwords)