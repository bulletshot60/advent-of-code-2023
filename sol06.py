import re

with open('input.txt') as file:
  times = [int(''.join([x for x in re.split("\s+", file.readline())[1:] if len(x) > 0]))]
  distances = [int(''.join([x for x in re.split("\s+", file.readline())[1:] if len(x) > 0]))]

total = 1
for i in range(len(times)):
  best = distances[i]
  ways_to_win = 0
  for j in range(0, times[i]):
    speed = j
    distance = speed * (times[i] - speed)
    if distance > best:
      ways_to_win += 1
  total *= ways_to_win
print(total)
