with open('input.txt') as f:
  lines = f.read().split("\n")

def get_next(listy):
  differences = [listy[i+1] - listy[i] for i in range(len(listy)-1)]
  if all([x == differences[0] for x in differences[1:]]):
    return listy[-1] + differences[0]
  else:
    return listy[-1] + get_next(differences)

def get_previous(listy):
  differences = [listy[i+1] - listy[i] for i in range(len(listy)-1)]
  if all([x == differences[0] for x in differences[1:]]):
    return listy[0] - differences[0]
  else:
    return listy[0] - get_previous(differences)

total = 0
for line in lines:
  total += get_previous(list(map(int, line.split(" "))))
print(total)
