with open('input.txt') as file:
    lines = [line.strip() for line in file]

horizontal = 0
depth = 0

for line in lines:
    if line.__contains__('forward'):
        horizontal += int(line[-1])
    elif line.__contains__('up'):
        depth -= int(line[-1])
    elif line.__contains__('down'):
        depth += int(line[-1])

print(horizontal * depth)
