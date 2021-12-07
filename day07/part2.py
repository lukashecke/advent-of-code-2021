with open('input.txt') as file:
    positions = list(map(int, file.readline().split(',')))

max_pos = max(positions)
min_pos = min(positions)

fuel_costs = {}

for i in range(min_pos, max_pos):
    fuel = 0
    for pos in positions:
        fuel += sum(range(abs(i - pos) + 1))
    fuel_costs[i] = fuel

print(min(fuel_costs.values()))
