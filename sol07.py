powers = {
  'A': 'm',
  'K': 'l',
  'Q': 'k',
  'T': 'j',
  '9': 'i',
  '8': 'h',
  '7': 'g',
  '6': 'f',
  '5': 'e',
  '4': 'd',
  '3': 'c',
  '2': 'b',
  'J': 'a',
}

def convert_hand_to_powers(hand):
  res = ''
  for card in hand:
    res += powers[card]
  return res

def get_type(hand):
  best = 0
  for alt in '23456789TQKA':
    cards = list(hand.replace('J', alt))
    uniq_cards = list(set(cards))
    counts = {x: cards.count(x) for x in uniq_cards}
    if len([card for card, count in counts.items() if count == 5]) == 1:
      best = max(best, 7)
    if len([card for card, count in counts.items() if count == 4]) == 1:
      best = max(best, 6)
    if len([card for card, count in counts.items() if count == 3]) == 1 and len([card for card, count in counts.items() if count == 2]) == 1:
      best = max(best, 5)
    if len([card for card, count in counts.items() if count == 3]) == 1:
      best = max(best, 4)
    if len([card for card, count in counts.items() if count == 2]) == 2:
      best = max(best, 3)
    if len([card for card, count in counts.items() if count == 2]) == 1:
      best = max(best, 2)
    if len([card for card, count in counts.items() if count == 1]) == 5:
      best = max(best, 1)
  return best
  

with open("input.txt", "r") as f:
  lines = [x.split(" ") for x in f.read().split("\n")]

to_sort = []
for line in lines:
  to_sort.append((get_type(line[0]), convert_hand_to_powers(line[0]), line[0], line[1]))

total = 0
rank = 1
for hand in sorted(to_sort):
  total += (int(hand[3]) * rank)
  rank += 1
print(total)
