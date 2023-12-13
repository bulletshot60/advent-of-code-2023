with open("input.txt") as f:
  lines = f.read().split("\n\n")

puzzles = []
for line in lines:
  puzzles.append(line.split("\n"))

def process_puzzle(puzzle):
  lines = []
  for i in range(1, len(puzzle) + 1):
    size = min(i, len(puzzle) - i)
    left = puzzle[i-size:i]
    right = puzzle[i:i+size][::-1]
    if len(left) > 0 and left == right:
      lines.append(i)
  return lines

def get_reflection_lines(puzzle):
  return {
    'horizontal': process_puzzle(puzzle),
    'vertical': process_puzzle([''.join([line[row] for line in puzzle]) for row in range(len(puzzle[0]))])
  }

def get_modified_puzzle(puzzle, original):
  res = {
    'horizontal': [],
    'vertical': []
  }
  for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
      new_puzzle = puzzle[:i] + [puzzle[i][:j] + ('#' if puzzle[i][j] == '.' else '.') + puzzle[i][j+1:]] + puzzle[i+1:]
      lines = get_reflection_lines(new_puzzle)
      for answer in lines['horizontal']:
        if answer not in original['horizontal'] and answer not in res["horizontal"]:
          res['horizontal'].append(answer)
      for answer in lines['vertical']:
        if answer not in original['vertical'] and answer not in res["vertical"]:
          res['vertical'].append(answer)
  return res

total = 0
for puzzle in puzzles:
  original_answer = get_reflection_lines(puzzle)
  print(original_answer)
  res = get_modified_puzzle(puzzle, original_answer)
  print(res)
  total += (sum(res['horizontal']) * 100 + sum(res['vertical']))

print(total)
