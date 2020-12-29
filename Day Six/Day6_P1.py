with open("C:\Programming\github\Advent-of-Code-2020\Day Six\Day6 Input.txt") as f:
    input = [line.strip() for line in f]

input.append("")    
answers, totalSum = [], 0

for answer in input:
    if answer == "":
        totalSum += len(answers)
        answers = []
    else:
        for c in answer:
            if c not in answers:
                answers.append(c)

print(totalSum)