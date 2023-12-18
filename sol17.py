import heapq

with open('input.txt') as f:
  lines = [[int(a) for a in line] for line in f.read().splitlines()]

def exists(node):
  return 0 <= node[X] < len(lines) and 0 <= node[Y] < len(lines[node[X]])

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

possible_dirs = {
  None: [SOUTH, EAST],
  NORTH: [EAST, WEST],
  EAST: [NORTH, SOUTH],
  SOUTH: [EAST, WEST],
  WEST: [NORTH, SOUTH],
}

X = 0
Y = 1

MIN_STEP = 4
MAX_STEP = 10

def process(start, end):
  queue = [(0, start, None, 1), (0, start, None, 1)]
  seen = set()
  while len(queue) > 0:
    cost, node, cur_dir, times_gone_this_dir = heapq.heappop(queue)
    if node == end:
      return cost
    if (node, cur_dir) in seen:
      continue
    seen.add((node, cur_dir))

    for dir in possible_dirs[cur_dir]:
      new_cost = cost
      new_times_gone_this_dir = 0
      if cur_dir == dir:
        new_times_gone_this_dir = times_gone_this_dir
      for step in range(1, MAX_STEP + 1):
        new_x = node[X] + dir[X] * step
        new_y = node[Y] + dir[Y] * step
        new_times_gone_this_dir += 1
        if exists((new_x, new_y)) and new_times_gone_this_dir <= MAX_STEP:
          new_cost += lines[new_x][new_y]
          if new_times_gone_this_dir >= MIN_STEP:
            heapq.heappush(queue, (new_cost, (new_x, new_y), dir, new_times_gone_this_dir))

result = process((0, 0), (len(lines) - 1, len(lines[-1]) - 1))
print(result)
