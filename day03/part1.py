with open('input.txt') as file:
    values = [line.strip() for line in file]

amount1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for num in values:
    for i in range(len(num)):
        if num[i] == '1':
            amount1[i] += 1

gammaStr = ''

for amount in amount1:
    if amount > (len(values) / 2):
        gammaStr += '1'
    else:
        gammaStr += '0'

gamma = int(gammaStr, 2)
epsilon = 0b111111111111 ^ gamma  # xor

print(gamma * epsilon)
