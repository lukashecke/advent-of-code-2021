with open('input.txt') as file:
    lines = [line.strip() for line in file]

horizontal = 0
depth = 0
aim = 0

for line in lines:
    if line.__contains__('forward'):
        horizontal += int(line[-1])
        if aim != 0:
            depth += int(line[-1]) * aim
    elif line.__contains__('up'):
        aim -= int(line[-1])
    elif line.__contains__('down'):
        aim += int(line[-1])

print(horizontal * depth)
