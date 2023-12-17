from os import linesep

with open('input.txt') as f:
  orig = [[a for a in line] for line in f.read().splitlines()]

def translate(cell):
  if cell == '.':
    return {'text': '.', 'dirs': {"N": ["N"], "E": ["E"], "S": ["S"], "W": ["W"]}, "ener": False}
  elif cell == '|':
    return {'text': '|', 'dirs': {"N": ["N"], "E": ["N", "S"], "S": ["S"], "W": ["N", "S"]}, "ener": False}
  elif cell == '-':
    return {'text': '-', 'dirs': {"N": ["E", "W"], "E": ["E"], "S": ["E", "W"], "W": ["W"]}, "ener": False}
  elif cell == '/':
    return {'text': '/', 'dirs': {"N": ["E"], "E": ["N"], "S": ["W"], "W": ["S"]}, "ener": False}
  elif cell == '\\':
    return {'text': '\\', 'dirs': {"N": ["W"], "E": ["S"], "S": ["E"], "W": ["N"]}, "ener": False}

def exists(pos):
  return 0 <= pos[0] < len(lines) and 0 <= pos[1] < len(lines[pos[0]])

def advance(pos, dir):
  if dir == 'E':
    return (pos[0], pos[1] + 1)
  elif dir == 'N':
    return (pos[0] - 1, pos[1])
  elif dir == 'S':
    return (pos[0] + 1, pos[1])
  elif dir == 'W':
    return (pos[0], pos[1] - 1)

def print_maze():
  for line in lines:
    for cell in line:
      if cell["ener"]:
        print('#', end='')
      else:
        print(cell["text"], end='')
    print()
  print()

def calc(start):
  last = [start]
  while len(last) > 0:
    now = []
    for cell in last:
      x, y, dir = cell
      lines[x][y]["ener"] = True
      if dir in lines[x][y]["dirs"]:
        for new_dir in lines[x][y]["dirs"][dir]:
          new_pos = advance((x, y), new_dir)
          if exists(new_pos):
            now.append((new_pos[0], new_pos[1], new_dir))
        del lines[x][y]["dirs"][dir]
    last = now[:]
  
  total = 0
  for x in range(len(lines)):
    for y in range(len(lines[x])):
      if lines[x][y]["ener"]:
        total += 1
  return total

def set_grid():
  global lines
  lines = [[translate(cell) for cell in line] for line in orig]

best = -1
for x in range(len(orig[0])): # top / bottom row
  set_grid()
  poss = calc((0, x, 'S'))
  best = max(best, poss)
  set_grid()
  poss = calc((len(orig) - 1, x, 'N'))
  best = max(best, poss)
for x in range(len(orig)): # left / right side
  set_grid()
  poss = calc((x, 0, 'E'))
  best = max(best, poss)
  set_grid()
  poss = calc((x, len(orig[0]) - 1, 'W'))
  best = max(best, poss)
print(best)
