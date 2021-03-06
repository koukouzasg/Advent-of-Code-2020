with open("C:\Programming\github\Advent-of-Code-2020\Day Five\Day5 Input.txt") as f:
	#input = f.readlines()
    #input = [passport for passport in f.read().split('\n\n')]
    input = [line.strip() for line in f]
    
maxSeatID = -1    
    
for seat in input:
    lower1, upper1, lower2, upper2, seat1, seat2 = 0, 127, 0, 7, 0, 0  
    
    for char in seat:
        if char == "F":          
            upper1 = (lower1+upper1)//2 
            seat1 = lower1
        elif char == "B":         
            lower1 = (lower1+upper1)//2 + 1
            seat1 = upper1
        elif char == "R":
            lower2 = (lower2+upper2)//2 + 1
            seat2 = upper2
        elif char == "L":
            upper2 = (lower2+upper2)//2
            seat2 = lower2
            
    seatID = seat1*8+seat2
    if seatID > maxSeatID:
        maxSeatID = seatID

print(maxSeatID)