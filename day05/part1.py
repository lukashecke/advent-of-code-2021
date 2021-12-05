lines = []

with open('input.txt') as file:
    for line in file.readlines():
        lines.append([list(map(int, line.split(','))) for line in line.strip().split(' -> ')])

relevant_lines = []  # only consider horizontal and vertical lines

for line in lines:
    if (line[0])[0] == (line[1])[0] or (line[0])[1] == (line[1])[1]:  # x1 = x2 or y1 = y2
        relevant_lines.append(line)

map = [[0]*1000 for i in range(1000)]


def points_between(points):
    points = []
    x1 = (line[0])[0]
    x2 = (line[1])[0]
    y1 = (line[0])[1]
    y2 = (line[1])[1]
    if x1 == x2:
        if y1 > y2:
            while y2 <= y1:
                points.append([x1, y2])
                y2 += 1
        else:  # y1 < y2
            while y1 <= y2:
                points.append([x1, y1])
                y1 += 1
            print()
    else:  # y1 = y2
        if x1 > x2:
            while x2 <= x1:
                points.append([x2, y1])
                x2 += 1
        else:  # x1 < x2
            while x1 <= x2:
                points.append([x1, y1])
                x1 += 1
    return points


for line in relevant_lines:
    for point in points_between(line):
        map[point[0]][point[1]] += 1

counter = 0

for j in range(1000):
    for i in range(1000):
        if map[i][j] >= 2:
            counter += 1

print(counter)
