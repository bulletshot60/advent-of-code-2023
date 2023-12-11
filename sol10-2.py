with open('input.txt') as f:
  lines = [[y for y in x] for x in f.read().split("\n")]

new_grid = [[{"char": ',', "dist": 0, "dirs": [], "orig": False}]]
for _ in range(len(lines[0])):
  new_grid[0].append({"char": ',', "dist": 0, "dirs": [], "orig": False})
  new_grid[0].append({"char": ',', "dist": 0, "dirs": [], "orig": False})
for x in range(len(lines)):
  new_row = [{"char": ',', "dist": 0, "dirs": [], "orig": False}]
  for y in range(len(lines[x])):
    if lines[x][y] == '|':
      new_row.append({"char": '|', "dist": 0, "dirs": ["N", "S"], "orig": True})
    if lines[x][y] == '-':
      new_row.append({"char": '─', "dist": 0, "dirs": ["E", "W"], "orig": True})
    if lines[x][y] == 'L':
      new_row.append({"char": '└', "dist": 0, "dirs": ["N", "E"], "orig": True})
    if lines[x][y] == 'J':
      new_row.append({"char": '┘', "dist": 0, "dirs": ["N", "W"], "orig": True})
    if lines[x][y] == '7':
      new_row.append({"char": '┐', "dist": 0, "dirs": ["S", "W"], "orig": True})
    if lines[x][y] == 'F':
      new_row.append({"char": '┌', "dist": 0, "dirs": ["S", "E"], "orig": True})
    if lines[x][y] == '.':
      new_row.append({"char": '.', "dist": 0, "dirs": [], "orig": True})
    if lines[x][y] == 'S':
      new_row.append({"char": 'S', "dist": 1, "dirs": ["N", "E", "S", "W"], "orig": True})
    new_row.append({"char": ',', "dist": 0, "dirs": [], "orig": False})
  new_grid.append(new_row)
  new_row = [{"char": ',', "dist": 0, "dirs": [], "orig": False}]
  for y in range(len(lines[x])):
    new_row.append({"char": ',', "dist": 0, "dirs": [], "orig": False})
    new_row.append({"char": ',', "dist": 0, "dirs": [], "orig": False})
  new_grid.append(new_row)

def exists(x, y):
  return 0 <= x < len(new_grid) and 0 <= y < len(new_grid[x])

def print_maze():
  for x in range(len(new_grid)):
    for y in range(len(new_grid[x])):
      if type(new_grid[x][y]) == dict:
        if new_grid[x][y]["dist"] >= 1:
          print(8, end='')
        else:
          print(new_grid[x][y]["char"], end='')
      else:
        print(new_grid[x][y], end='')
    print()
  print()

def is_outside(x, y):
  return x == 0 or x == len(new_grid) - 1 or y == 0 or y == len(new_grid[x]) - 1

def mark(x, y):
  marked = [(x, y)]
  while marked != []:
    new_marked = []
    for mark in marked:
      if exists(mark[0], mark[1]) and new_grid[mark[0]][mark[1]]['char'] in ['.', ',']:
        new_grid[mark[0]][mark[1]]['char'] = 'x'
        new_marked.append((mark[0] - 1, mark[1]))
        new_marked.append((mark[0] + 1, mark[1]))
        new_marked.append((mark[0], mark[1] - 1))
        new_marked.append((mark[0], mark[1] + 1))
    marked = new_marked[:]

points = []
for x in range(len(new_grid)):
  for y in range(len(new_grid[x])):
    if new_grid[x][y]['char'] == ',':
      if (exists(x - 1, y) and "S" in new_grid[x - 1][y]['dirs']) or (exists(x + 1, y) and "N" in new_grid[x + 1][y]['dirs']):
        new_grid[x][y] = {"char": '|', "dist": 0, "dirs": ["N", "S"], "orig": False}
      if (exists(x, y - 1) and "E" in new_grid[x][y - 1]['dirs']) or (exists(x, y + 1) and "W" in new_grid[x][y + 1]['dirs']):
        new_grid[x][y] = {"char": '─', "dist": 0, "dirs": ["E", "W"], "orig": False}
    if new_grid[x][y]['char'] == 'S':
      points.append((x, y))

# print_maze()

best = 1
while len(points) > 0:
  new_points = []
  for x, y in points:
    if new_grid[x][y]["dist"] == best:
      if exists(x - 1, y) and "N" in new_grid[x][y]["dirs"] and "S" in new_grid[x - 1][y]["dirs"]:
        if new_grid[x][y]["dist"] + 1 >= new_grid[x-1][y]["dist"]:
          new_grid[x-1][y]["dist"] = new_grid[x][y]["dist"] + 1
          new_grid[x][y]["dirs"].remove("N")
          new_grid[x-1][y]["dirs"].remove("S")
          new_points.append((x - 1, y))
      if exists(x + 1, y) and "S" in new_grid[x][y]["dirs"] and "N" in new_grid[x + 1][y]["dirs"]:
        if new_grid[x][y]["dist"] + 1 >= new_grid[x+1][y]["dist"]:
          new_grid[x+1][y]["dist"] = new_grid[x][y]["dist"] + 1
          new_grid[x][y]["dirs"].remove("S")
          new_grid[x+1][y]["dirs"].remove("N")
          new_points.append((x + 1, y))
      if exists(x, y - 1) and "W" in new_grid[x][y]["dirs"] and "E" in new_grid[x][y - 1]["dirs"]:
        if new_grid[x][y]["dist"] + 1 >= new_grid[x][y-1]["dist"]:
          new_grid[x][y-1]["dist"] = new_grid[x][y]["dist"] + 1
          new_grid[x][y]["dirs"].remove("W")
          new_grid[x][y-1]["dirs"].remove("E")
          new_points.append((x, y - 1))
      if exists(x, y + 1) and "E" in new_grid[x][y]["dirs"] and "W" in new_grid[x][y + 1]["dirs"]:
        if new_grid[x][y]["dist"] + 1 >= new_grid[x][y+1]["dist"]:
          new_grid[x][y+1]["dist"] = new_grid[x][y]["dist"] + 1
          new_grid[x][y]["dirs"].remove("E")
          new_grid[x][y+1]["dirs"].remove("W")
          new_points.append((x, y + 1))
  best += 1
  points = new_points[:]

for x in range(len(new_grid)):
  for y in range(len(new_grid[x])):
    if len(new_grid[x][y]['dirs']) > 0 and new_grid[x][y]['dist'] == 0 and new_grid[x][y]['orig']:
      new_grid[x][y]['char'] = '.'
      new_grid[x][y]['dirs'] = []
    if len(new_grid[x][y]['dirs']) > 0 and new_grid[x][y]['dist'] == 0 and not new_grid[x][y]['orig']:
      new_grid[x][y]['char'] = ','
      new_grid[x][y]['dirs'] = []

for x in range(len(new_grid)):
  for y in range(len(new_grid[x])):
    if is_outside(x, y) and new_grid[x][y]['char'] in ['.', ',']:
      mark(x, y)

total = 0
for x in range(len(new_grid)):
  for y in range(len(new_grid[x])):
    if new_grid[x][y]['char'] == '.':
      total += 1

# print_maze()

print(total)
