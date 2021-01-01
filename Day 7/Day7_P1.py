import queue

with open("C:\Programming\github\Advent-of-Code-2020\Day 7\Day7 Input.txt") as f:
    input = [line.strip() for line in f]

checked, q = set(), queue.Queue() 
q.put("shiny gold")

while not q.empty():
        color = q.get()
        for line in input:
            if color in line and line.index(color) != 0:
                tempLine = line.split()
                temp_color = tempLine[0]+ " " + tempLine[1]
                if temp_color not in checked:
                    q.put(temp_color)
                    checked.add(temp_color)

print(checked, len(checked))