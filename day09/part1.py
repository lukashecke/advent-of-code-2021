with open('input.txt') as file:
    input = file.read()

map = [list(map(int, list(line))) for line in input.split('\n')]

risk_level = 0

for y in range(100):
    check = 0
    for x in range(100):
        if x > 0 and x < 99 and y > 0 and y < 99:  # all 'middle' numbers
            if map[x][y] < map[x - 1][y]:  # left
                if map[x][y] < map[x][y - 1]:  # top
                    if map[x][y] < map[x + 1][y]:  # right
                        if map[x][y] < map[x][y + 1]:  # bottom
                            risk_level += map[x][y] + 1
        elif x > 0 and x < 99 and y == 0:  # all top 'middle' numbers
            if map[x][y] < map[x - 1][y]:  # left
                if map[x][y] < map[x + 1][y]:  # right
                    if map[x][y] < map[x][y + 1]:  # bottom
                        risk_level += map[x][y] + 1
        elif x == 0 and y > 0 and y < 99:  # all left 'middle' numbers
            if map[x][y] < map[x][y - 1]:  # top
                if map[x][y] < map[x + 1][y]:  # right
                    if map[x][y] < map[x][y + 1]:  # bottom
                        risk_level += map[x][y] + 1
        elif x == 99 and y > 0 and y < 99:  # all right 'middle' numbers
            if map[x][y] < map[x][y - 1]:  # top
                if map[x][y] < map[x - 1][y]:  # left
                    if map[x][y] < map[x][y + 1]:  # bottom
                        risk_level += map[x][y] + 1
        elif x > 0 and x < 99 and y == 99:  # all bottom 'middle' numbers
            if map[x][y] < map[x - 1][y]:  # left
                if map[x][y] < map[x][y - 1]:  # top
                    if map[x][y] < map[x + 1][y]:  # right
                        risk_level += map[x][y] + 1
        elif x == 0 and y == 0:  # top left number
            if map[x][y] < map[x + 1][y]:  # right
                if map[x][y] < map[x][y + 1]:  # bottom
                    risk_level += map[x][y] + 1
        elif x == 99 and y == 0:  # top right number
            if map[x][y] < map[x - 1][y]:  # left
                if map[x][y] < map[x][y + 1]:  # bottom
                    risk_level += map[x][y] + 1
        elif x == 0 and y == 99:  # bottom left number
            if map[x][y] < map[x][y - 1]:  # top
                if map[x][y] < map[x + 1][y]:  # right
                    risk_level += map[x][y] + 1
        elif x == 99 and y == 99:  # bottom right number
            if map[x][y] < map[x - 1][y]:  # left
                if map[x][y] < map[x][y - 1]:  # top
                    risk_level += map[x][y] + 1

print(risk_level)
