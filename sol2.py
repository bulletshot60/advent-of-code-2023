games = {}
with open('input.txt') as file:
    lines = file.read().split('\n')
    for line in lines:
        before, after = line.split(": ")
        games[int(before.split(' ')[1])] = [
            [(color.split(' ')[1], int(color.split(' ')[0])) for color in drawing.split(', ')] for drawing in after.split('; ')
        ]

total = 0
for key, game in games.items():
    local_max = {}
    for drawing in game:
        for color in drawing:
            if color[0] not in local_max or local_max[color[0]] < color[1]:
                local_max[color[0]] = color[1]
    power = (local_max['red'] if 'red' in local_max else 1) * (local_max['green'] if 'green' in local_max else 1) * (local_max['blue'] if 'blue' in local_max else 1)
    total += power
print(total)
            