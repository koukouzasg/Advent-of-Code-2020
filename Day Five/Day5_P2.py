with open("C:\Programming\github\Advent-of-Code-2020\Day Five\Day5 Input.txt") as f:
    input = [line.strip() for line in f]
    
seat_ids = []  
    
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
    seat_ids.append(seatID)
    
seat_ids.sort()

for i, seatID in enumerate(seat_ids):
    if i == len(seat_ids)-1:
        break
    if i > 0 and seat_ids[i+1]-seatID == 2:
        print(seatID+1)