with open("C:\Programming\Advent of Code2020\Day1 Input.txt") as f:
    input = f.readlines()

input = [int(numeric_string) for numeric_string in input]

a = 0
b = 0
c = 0

for i in input:
    for j in input:
        for k in input:
            if i+j+k == 2020:
                a = i
                b = j
                c = k
                break

print(" Number 1 :", a,"\n", "Number 2 :", b,"\n", "Number 3 :", c,"\n","Result :", a*b*c,"\n")
