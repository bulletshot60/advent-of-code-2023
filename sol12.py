from functools import cache

with open('input.txt') as f:
  lines = f.read().split("\n")

@cache
def recurse(puzzle, groups):
  if len(puzzle) == 0 and len(groups) == 0:
    return 1
  if len(groups) == 0 and '#' not in puzzle:
    return 1
  if len(puzzle) == 0 or len(groups) == 0:
    return 0

  tot = 0
  if puzzle[0] in ".?":
    tot += recurse(puzzle[1:], groups)
  if puzzle[0] in "#?" and groups[0] <= len(puzzle) and '.' not in puzzle[:groups[0]] and (groups[0] == len(puzzle) or puzzle[groups[0]] != '#'):
    tot += recurse(puzzle[groups[0] + 1:], groups[1:])
  return tot

total = 0
for line in lines:
  puzzle, group = line.split(" ")
  puzzle = '?'.join([puzzle for _ in range(5)])
  group = ','.join([group for _ in range(5)])
  groups = tuple(map(int, group.split(",")))
  total += recurse(puzzle, groups)
print(total)
