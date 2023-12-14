with open("input.txt") as f:
  lines = f.read().split("\n")

matrix = [[a for a in line] for line in lines]

def rotate_left():
  global matrix
  matrix = [list(x) for x in list(zip(*matrix[::-1]))]

def tilt():
  column_height = [-1] * len(matrix[0])
  for x in range(len(matrix)):
    for y in range(len(matrix[x])):
      if matrix[x][y] == "#":
        column_height[y] = x
      if matrix[x][y] == "O":
        matrix[x][y] = '.'
        column_height[y] += 1
        matrix[column_height[y]][y] = 'O'

def load():
  total = 0
  for x in range(len(matrix)):
    for y in range(len(matrix[x])):
      if matrix[x][y] == "O":
        total += len(lines) - x
  return total

def print_dish():
  for x in range(len(matrix)):
    for y in range(len(matrix[x])):
      print(matrix[x][y], end="")
    print()
  print()

def stringify(matrix):
  return "\n".join(["".join(row) for row in matrix])

first = True
previous_matrixes = []
while stringify(matrix) not in previous_matrixes:
  if not first:
    previous_matrixes.append(stringify(matrix))
  else:
    first = False
  tilt()
  rotate_left()
  tilt()
  rotate_left()
  tilt()
  rotate_left()
  tilt()
  rotate_left()

loop_end = previous_matrixes.index(stringify(matrix))
period = len(previous_matrixes) - loop_end
pos = (1000000000 - loop_end) % period + loop_end - 1
matrix = [[a for a in line] for line in previous_matrixes[pos].split("\n")]

print_dish()
print(load())
