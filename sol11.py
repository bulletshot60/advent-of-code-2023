with open("input.txt", "r") as f:
  lines = f.read().split("\n")

MULTIPLIER = 1000000

# add rows
double_row = []
for row in range(len(lines)):
  if all([x == '.' for x in lines[row]]):
    double_row.append(row)

double_col = []
for col in range(len(lines[0])):
  column = [line[col] for line in lines]
  if all([x == '.' for x in column]):
    double_col.append(col)

i = 1
points = {}
row_pad = 0
for x in range(len(lines)):
  if x in double_row:
    row_pad += MULTIPLIER - 1
  col_pad = 0
  for y in range(len(lines[x])):
    if y in double_col:
      col_pad += MULTIPLIER - 1
    if lines[x][y] == '#':
      points[i] = (x + row_pad, y + col_pad)
      i += 1

total = 0
for i in range(1, len(points) + 1):
  for j in range(i, len(points) + 1):
    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
    total += dist

print(total)
