import collections

with open("C:\Programming\github\Advent-of-Code-2020\Day Six\Day6 Input.txt") as f:
    input = [line.strip() for line in f]

input.append("")    
answers, totalSum, linesCounter = [], 0, 0

for answer in input:
    if answer == "":
        frequencies = collections.Counter(answers)
        repeated = {}
        for key, value in frequencies.items():
            if value == linesCounter:
                totalSum += 1
        answers = []
        linesCounter = 0
    else:
        linesCounter += 1
        for c in answer:
            answers.append(c)

print(totalSum)