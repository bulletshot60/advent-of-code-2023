with open('input.txt') as file:
    lines = file.read().split("\n")

def get_number(row, col):
    num = lines[row][col]
    temp_col = col - 1
    while temp_col >= 0 and lines[row][temp_col].isdigit():
        num = lines[row][temp_col] + num
        temp_col -= 1
    temp_col = col + 1
    while temp_col < len(lines[row]) and lines[row][temp_col].isdigit():
        num = num + lines[row][temp_col]
        temp_col += 1
    return int(num)

total = 0
for row in range(len(lines)):
    for col in range(len(lines[row])):
        numbers = []
        if lines[row][col] == '*':
            if row - 1 >= 0:
                if lines[row-1][col].isdigit():
                    numbers.append(get_number(row-1, col))
                else:
                    if col - 1 >= 0 and lines[row-1][col-1].isdigit():
                        numbers.append(get_number(row-1, col-1))
                    if col + 1 < len(lines[row]) and lines[row-1][col+1].isdigit():
                        numbers.append(get_number(row-1, col+1))
            if col - 1 >= 0 and lines[row][col-1].isdigit():
                numbers.append(get_number(row, col-1))
            if col + 1 < len(lines[row]) and lines[row][col+1].isdigit():
                numbers.append(get_number(row, col+1))
            if row + 1 < len(lines):
                if lines[row+1][col].isdigit():
                    numbers.append(get_number(row+1, col))
                else:
                    if col - 1 >= 0 and lines[row+1][col-1].isdigit():
                        numbers.append(get_number(row+1, col-1))
                    if col + 1 < len(lines[row]) and lines[row+1][col+1].isdigit():
                        numbers.append(get_number(row+1, col+1))
            if len(numbers) == 2:
                total += numbers[0] * numbers[1]
            
print(total)
        
