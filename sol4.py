with open('input.txt') as file:
    lines = file.read().split("\n")

card_count = {i: 1 for i in range(1, len(lines) + 1)}

card = 1
for line in lines:
    winning, scratched = line.split(": ")[1].split(" | ")
    winning, scratched = [int(x) for x in winning.split(" ") if x != ''], [int(x) for x in scratched.split(" ") if x != '']
    won = len(list(set(winning) & set(scratched)))
    if won > 0:
        for i in range(card + 1, min(card + 1 + won, len(lines) + 1)):
            card_count[i] += card_count[card]
    card += 1

print(sum(card_count.values()))