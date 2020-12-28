def caluclate_Trees(input, right, down):
    x, y, trees = (0, 0, 0)

    maximumX = len(input[0])

    while y < len(input) - down:
        x += right
        y += down
        if x >= maximumX:
            x = x - maximumX
        if input[y][x] == "#":
            trees += 1
    return trees

with open("C:\Programming\Advent of Code2020\Day Three\Day3 Input.txt")as f:
	input = f.readlines()

input = [x.strip() for x in input]	

print(caluclate_Trees(input, 1, 1)*
    caluclate_Trees(input, 3, 1)*
    caluclate_Trees(input, 5, 1)*
    caluclate_Trees(input, 7, 1)*
    caluclate_Trees(input, 1, 2) )