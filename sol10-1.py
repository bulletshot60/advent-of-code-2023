import time

with open('input.txt') as f:
  lines = [[y for y in x] for x in f.read().split("\n")]

points = []

for x in range(len(lines)):
  for y in range(len(lines[x])):
    if lines[x][y] == '|':
      lines[x][y] = {"dist": 0, "dirs": ["N", "S"]}
    if lines[x][y] == '-':
      lines[x][y] = {"dist": 0, "dirs": ["E", "W"]}
    if lines[x][y] == 'L':
      lines[x][y] = {"dist": 0, "dirs": ["N", "E"]}
    if lines[x][y] == 'J':
      lines[x][y] = {"dist": 0, "dirs": ["N", "W"]}
    if lines[x][y] == '7':
      lines[x][y] = {"dist": 0, "dirs": ["S", "W"]}
    if lines[x][y] == 'F':
      lines[x][y] = {"dist": 0, "dirs": ["S", "E"]}
    if lines[x][y] == "S":
      lines[x][y] = {"dist": 1, "dirs": ["N", "E", "S", "W"]}
      points.append((x, y))

def exists(x, y) -> bool:
  if 0 <= x < len(lines) and 0 <= y < len(lines[x]) and type(lines[x][y]) == dict:
    return True
  return False

def print_maze():
  for x in range(len(lines)):
    for y in range(len(lines[x])):
      if type(lines[x][y]) == dict:
        print(lines[x][y]["dist"], end='')
      else:
        print(lines[x][y], end='')
    print()
  print()
  time.sleep(1)

best = 1
while len(points) > 0:
  new_points = []
  for x, y in points:
    if lines[x][y]["dist"] == best:
      if exists(x - 1, y) and "N" in lines[x][y]["dirs"] and "S" in lines[x - 1][y]["dirs"]:
        if lines[x][y]["dist"] + 1 >= lines[x-1][y]["dist"]:
          lines[x-1][y]["dist"] = lines[x][y]["dist"] + 1
          lines[x][y]["dirs"].remove("N")
          lines[x-1][y]["dirs"].remove("S")
          new_points.append((x - 1, y))
      if exists(x + 1, y) and "S" in lines[x][y]["dirs"] and "N" in lines[x + 1][y]["dirs"]:
        if lines[x][y]["dist"] + 1 >= lines[x+1][y]["dist"]:
          lines[x+1][y]["dist"] = lines[x][y]["dist"] + 1
          lines[x][y]["dirs"].remove("S")
          lines[x+1][y]["dirs"].remove("N")
          new_points.append((x + 1, y))
      if exists(x, y - 1) and "W" in lines[x][y]["dirs"] and "E" in lines[x][y - 1]["dirs"]:
        if lines[x][y]["dist"] + 1 >= lines[x][y-1]["dist"]:
          lines[x][y-1]["dist"] = lines[x][y]["dist"] + 1
          lines[x][y]["dirs"].remove("W")
          lines[x][y-1]["dirs"].remove("E")
          new_points.append((x, y - 1))
      if exists(x, y + 1) and "E" in lines[x][y]["dirs"] and "W" in lines[x][y + 1]["dirs"]:
        if lines[x][y]["dist"] + 1 >= lines[x][y+1]["dist"]:
          lines[x][y+1]["dist"] = lines[x][y]["dist"] + 1
          lines[x][y]["dirs"].remove("E")
          lines[x][y+1]["dirs"].remove("W")
          new_points.append((x, y + 1))
  best += 1
  points = new_points[:]
  # print_maze()
print(best - 2)
