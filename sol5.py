with open("input.txt") as file:
  lines = file.read().split("\n")

  seeds = list(map(int, lines[0].split(": ")[1].split(" ")))

  upper_map = {}
  category_map = {}
  f, t = None, None
  for category_maps in lines[2:]:
    if len(category_maps) > 0:
      if category_maps[0].isalpha():
        f, _, t = category_maps.replace(" map:", "").split("-")
        upper_map[f] = t
      elif category_maps[0].isdigit():
        to, start, l = map(int, category_maps.split(" "))
        if f not in category_map:
          category_map[f] = {}
        category_map[f][(start, start + l)] = (to, to + l)

  lowest = -1
  for i in range(0, len(seeds), 2):
    for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
      current = 'seed'
      while current != 'location':
        for mapping in category_map[current]:
          if mapping[0] <= seed < mapping[1]:
            seed = category_map[current][mapping][0] + (seed - mapping[0])
            break
        current = upper_map[current]
      if lowest == -1 or seed < lowest:
        lowest = seed
  print(lowest)
