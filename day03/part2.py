with open('input.txt') as file:
    values = [line.strip() for line in file]
    

def more_used_bit(array, position):
    amount_of_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in array:
        for i in range(len(num)):
            if num[i] == '1':
                amount_of_1[i] += 1

    more_used = ''

    for amount in amount_of_1:
        if amount >= (len(array) / 2):
            more_used += '1'
        else:
            more_used += '0'
    return more_used[position]


filtered = values
oxygen = 0

for i in range(len(values)):
    if len(filtered) == 1:
        oxygen = int(filtered[0], 2)
        break
    else:
        filtered = list(filter(lambda x: x[i] == more_used_bit(filtered, i), filtered))


def less_used_bit(array, position):
    amount_of_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in array:
        for i in range(len(num)):
            if num[i] == '1':
                amount_of_1[i] += 1

    less_used = ''

    for amount in amount_of_1:
        if amount >= (len(array) / 2):
            less_used += '0'
        else:
            less_used += '1'
    return less_used[position]


filtered = values
co2 = 0

for i in range(len(values)):
    if len(filtered) == 1:
        co2 = int(filtered[0], 2)
        break
    else:
        filtered = list(filter(lambda x: x[i] == less_used_bit(filtered, i), filtered))

print(oxygen * co2)
