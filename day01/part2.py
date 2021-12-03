import sys

with open('input.txt') as file:
    values = [int(line) for line in file]

sums = [None] * (len(values) - 2)

for i in range(len(sums)):
    sums[i] = values[i] + values[i + 1] + values[i + 2]

prev = sys.maxsize
counter = 0

for num in sums:
    if num > prev:
        counter += 1
    prev = num

print(counter)
