with open('input.txt') as file:
    input = file.read()

map = [list(map(int, list(j))) for j in input.split('\n')]

risk_level = 0

for j in range(100):
    check = 0
    for i in range(100):
        if i > 0 and i < 99 and j > 0 and j < 99:  # all 'middle' numbers
            if map[i][j] < map[i][j - 1]:  # left
                if map[i][j] < map[i - 1][j]:  # top
                    if map[i][j] < map[i][j + 1]:  # right
                        if map[i][j] < map[i + 1][j]:  # bottom
                            risk_level += map[i][j] + 1
        if i == 0 and j > 0 and j < 99:  # all top 'middle' numbers
            if map[i][j] < map[i][j - 1]:  # left
                if map[i][j] < map[i][j + 1]:  # right
                    if map[i][j] < map[i + 1][j]:  # bottom
                        risk_level += map[i][j] + 1
        if i > 0 and i < 99 and j == 0:  # all left 'middle' numbers
            if map[i][j] < map[i - 1][j]:  # top
                if map[i][j] < map[i][j + 1]:  # right
                    if map[i][j] < map[i + 1][j]:  # bottom
                        risk_level += map[i][j] + 1
        if i > 0 and i < 99 and j == 99:  # all right 'middle' numbers
            if map[i][j] < map[i - 1][j]:  # top
                if map[i][j] < map[i][j - 1]:  # left
                    if map[i][j] < map[i + 1][j]:  # bottom
                        risk_level += map[i][j] + 1
        if i == 99 and j > 0 and j < 99:  # all bottom 'middle' numbers
            if map[i][j] < map[i][j - 1]:  # left
                if map[i][j] < map[i - 1][j]:  # top
                    if map[i][j] < map[i][j + 1]:  # right
                        risk_level += map[i][j] + 1
        if i == 0 and j == 0:  # top left number
            if map[i][j] < map[i][j + 1]:  # right
                if map[i][j] < map[i + 1][j]:  # bottom
                    risk_level += map[i][j] + 1
        if i == 0 and j == 99:  # top right number
            if map[i][j] < map[i][j - 1]:  # left
                if map[i][j] < map[i + 1][j]:  # bottom
                    risk_level += map[i][j] + 1
        if i == 99 and j == 0:  # bottom left number
            if map[i][j] < map[i - 1][j]:  # top
                if map[i][j] < map[i][j + 1]:  # right
                    risk_level += map[i][j] + 1
        if i == 99 and j == 99:  # bottom right number
            if map[i][j] < map[i][j - 1]:  # left
                if map[i][j] < map[i - 1][j]:  # top
                    risk_level += map[i][j] + 1

print(risk_level)
