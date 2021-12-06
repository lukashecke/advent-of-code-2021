with open('input.txt') as file:
    input = list(map(int, file.readline().split(',')))

fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

for num in input:
    fish[num] += 1

day = 0

while day < 256:
    amount_birth = fish[0]
    fish[0] = fish[1]
    fish[1] = fish[2]
    fish[2] = fish[3]
    fish[3] = fish[4]
    fish[4] = fish[5]
    fish[5] = fish[6]
    fish[6] = fish[7]
    fish[7] = fish[8]
    fish[8] = amount_birth
    fish[6] += amount_birth
    day += 1

print(sum(fish.values()))
