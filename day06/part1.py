with open('input.txt') as file:
    lanternfish = list(map(int, file.readline().split(',')))

day = 0

while day < 80:
    amount_of_fish = len(lanternfish)
    for i in range(amount_of_fish):
        if lanternfish[i] == 0:
            lanternfish[i] = 7  # -1 in line 13
            lanternfish.append(8)
            amount_of_fish += 1
        lanternfish[i] -= 1
    day += 1

print(len(lanternfish))
