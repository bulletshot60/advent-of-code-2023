with open("input.txt", "r") as f:
  lines = f.read().split(",")

boxes = {i: [] for i in range(256)}

def hash(string):
  current = 0
  for c in string:
    current += ord(c)
    current *= 17
    current %= 256
  return current

def index_of_lens(box, label):
  for i in range(len(boxes[box])):
    if boxes[box][i][0] == label:
      return i
  return -1

def remove_lens(box, label):
  idx = index_of_lens(box, label)
  if idx >= 0:
    boxes[box].pop(idx)

def add_lens(box, label, fl):
  idx = index_of_lens(box, label)
  if idx >= 0:
    boxes[box][idx] = (label, fl)
  else:
    boxes[box].append((label, fl))

def print_boxes():
  for i in range(256):
    if len(boxes[i]) > 0:
      print(f"{i}: {boxes[i]}")

for line in lines:
  if '-' in line:
    label, _ = line.split("-")
    box = hash(label)
    remove_lens(box, label)
  elif '=' in line:
    label, fl = line.split("=")
    box = hash(label)
    add_lens(box, label, int(fl))
  # print_boxes()

total = 0
for box in range(256):
  for slot in range(len(boxes[box])):
    total += (1 + box) * (1 + slot) * boxes[box][slot][1]
print(total)
