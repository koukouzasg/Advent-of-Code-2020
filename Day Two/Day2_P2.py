with open("C:\Programming\Advent of Code2020\Day Two\Day2 Input.txt") as f:
    input = f.readlines()

valid_passwords = 0    
  
for line in input:
    temp = line.split("-")
    pos1 = int(temp[0]) - 1
    temp = temp[1].split()
    pos2 = int(temp[0]) - 1
    restriction = temp[1]
    restriction = restriction[0]
    password = temp[2]
    
    foo = ([pos for pos, char in enumerate(password) if char == restriction])
    if ( ((pos1 in foo) and (pos2 not in foo)) or ((pos1 not in foo) and (pos2 in foo)) ):
        valid_passwords += 1

print (valid_passwords)