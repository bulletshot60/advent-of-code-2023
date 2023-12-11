from math import gcd
import itertools

with open('input.txt') as f:
  lines = f.read().split("\n")

commands = list(lines[0])

nodes = {}
for node in lines[2:]:
  parts = node.split(" = ")
  left, right = parts[1].strip("()").split(", ")
  nodes[parts[0]] = {"L": left, "R": right}

start_nodes = {node: 0 for node, dirs in nodes.items() if node.endswith("A")}
for start in start_nodes:
  steps = 0
  node = start[:]
  for command in itertools.cycle(commands):
    if node.endswith('Z'):
      break
    else:
      node = nodes[node][command]
      steps += 1
  start_nodes[start] = steps

lcm = 1
for i in list(start_nodes.values()):
  lcm = lcm * i // gcd(lcm, i)
print(lcm)
