from math import dist

with open("input.txt") as f:
  lines = f.read().splitlines()

grid = []
for x in range(1000):
  grid.append([0] * 1000)

dirs = {
  'U': (0, -1),
  'D': (0, 1),
  'L': (-1, 0),
  'R': (1, 0)
}

outside_dist = 0
points = [(0, 0)]
for line in lines:
  _, _, color = line.split(" ")

  color = color[2:-1]
  length = int(color[:5], 16)
  dir = color[5:]

  if dir == '0':
    dir = 'R'
  elif dir == '1':
    dir = 'D'
  elif dir == '2':
    dir = 'L'
  elif dir == '3':
    dir = 'U'
  
  prev = points[-1]
  length = int(length)
  points.append((
    prev[0] + length * dirs[dir][0],
    prev[1] + length * dirs[dir][1]
  ))
  outside_dist += dist(points[-1], points[-2])

inside_dist = 0.0
for i in range(len(points) - 1):
  inside_dist += (points[i][0] * points[i+1][1] - points[i][1] * points[i+1][0])

print((outside_dist + inside_dist) // 2 + 1)
