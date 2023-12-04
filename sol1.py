with open('input.txt') as file:
  lines = file.read().split('\n')

replacements = {
  'one': 'on1e',
  'two': 'tw2o',
  'three': 'thre3e',
  'four': 'fou4r',
  'five': 'fiv5e',
  'six': 'si6x',
  'seven': 'seve7n',
  'eight': 'eigh8t',
  'nine': 'nin9e',
}

def replace(s: str):
  for orig, repl in replacements.items():
    s = s.replace(orig, repl)
  return s

lines = [replace(line) for line in lines]
lines = [[ch for ch in line if ch.isdigit()] for line in lines]
lines = [int(x[0] + x[-1]) for x in lines]
print(sum(lines))