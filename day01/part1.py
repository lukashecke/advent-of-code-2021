import sys

with open('input.txt') as file:
    values = [int(line) for line in file]

prev = sys.maxsize
counter = 0

for num in values:
    if num > prev:
        counter += 1
    prev = num

print(counter)
