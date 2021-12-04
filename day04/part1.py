with open('input.txt') as file:
    chosen_numbers = list(map(int, file.readline().split(',')))

with open('input.txt') as file:
    cards_numbers = list(file.read().split('\n\n'))

cards_numbers.pop(0)  # first line are just the chosen numbers

cards = []

for card_numbers in cards_numbers:
    cards.append([list(map(int, j.split())) for j in card_numbers.split('\n')])

# idea: marking numbers by adding 100


def check_for_winner_vertical(card):
    for j in range(5):
        check = 0
        for i in range(5):
            if card[i][j] >= 100:
                check += 1
        if check >= 5:  # every number had to be marked
            return True


def check_for_winner_horizontal(card):
    for i in range(5):
        check = 0
        for j in range(5):
            if card[i][j] >= 100:
                check += 1
        if check >= 5:  # every number had to be marked
            return True


def mark_number(number):
    for card in cards:
        for j in range(5):
            for i in range(5):
                if card[i][j] == number:
                    card[i][j] += 100
                    if check_for_winner_horizontal(card):
                        return card
                    if check_for_winner_vertical(card):
                        return card


def calc_score(card, number):
    sum_unmarked = 0
    for j in range(5):
        for i in range(5):
            if card[i][j] < 100:
                sum_unmarked += card[i][j]
    return sum_unmarked * number


for number in chosen_numbers:
    winning_card = mark_number(number)
    if winning_card is not None:
        print(calc_score(winning_card, number))
        break
