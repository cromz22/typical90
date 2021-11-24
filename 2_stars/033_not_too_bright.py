height, width = map(int, input().split())

# Naive idea O(2**hw)
# 1. Generate all possible states
# 2. Check if they are valid and store the number of illuminated LEDs
# 3. Output the max of the stored values

# Heuristic idea
if width == 1 or height == 1:
    answer = width * height
else:
    row_max = width / 2 if width % 2 == 0 else (width + 1) / 2
    column_max = height / 2 if height % 2 == 0 else (height + 1) / 2
    answer = int(row_max * column_max)
print(answer)
