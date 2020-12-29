with open("C:\Programming\github\Advent-of-Code-2020\Day Six\Day6 Input.txt") as f:
    input = [line.strip() for line in f]

input.append("")    
answers, totalSum = [], 0

for i, answer in enumerate(input):
    if answer == "":
        #totalSum += len(answers)
        print(answers)
        break
        answers = []
    else:
        answers.append(answer)
  

print(totalSum)