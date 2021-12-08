with open('input.txt') as file:
    output_values = [line.strip().split(' | ')[1] for line in file]

ones = 0
fours = 0
sevens = 0
eights = 0

for value in output_values:
    for segment in value.split(' '):
        if len(segment) == 2:
            ones += 1
        if len(segment) == 4:
            fours += 1
        if len(segment) == 3:
            sevens += 1
        if len(segment) == 7:
            eights += 1

print(ones + fours + sevens + eights)
