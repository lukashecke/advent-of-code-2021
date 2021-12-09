with open('input.txt') as file:
    input = file.read()

map = [list(map(int, list(line))) for line in input.split('\n')]
basin_size = 0


def flood_map(x, y):
    if x >= 0 and x <= 99 and y >= 0 and y <= 99:
        if map[x][y] is not 9:
            map[x][y] = 9
            global basin_size
            basin_size += 1
            flood_map(x - 1, y)  # left
            flood_map(x, y - 1)  # top
            flood_map(x + 1, y)  # right
            flood_map(x, y + 1)  # bottom


basin_sizes = []

for y in range(100):
    check = 0
    for x in range(100):
        if map[x][y] is not 9:
            basin_size = 0
            flood_map(x, y)
            basin_sizes.append(basin_size)

basin_sizes.sort(reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
