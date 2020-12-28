with open("C:\Programming\Advent of Code2020\Day Three\Day3 Input.txt")as f:
	input = f.readlines()

input = [x.strip() for x in input]	
x, y, trees = (0, 0, 0)

maximumX = len(input[0])

while y < len(input)-1:
    x += 3
    y += 1
    if x >= maximumX:
        x = x - maximumX
    if input[y][x] == "#":
        trees += 1
    
print(trees)