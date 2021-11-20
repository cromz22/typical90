import numpy as np


# read input
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a = np.array(a, dtype=int)


# plan
# 1. calculate the sum of each row/column
# 2. for each cell, sum the two values from them that corresponds to the cell position, and subtract the value of the cell
row_sums = np.sum(a, axis=1)
col_sums = np.sum(a, axis=0)

b = np.zeros((n, m), dtype=int)
for i in range(n):
    for j in range(m):
        b[i][j] = row_sums[i] + col_sums[j] - a[i][j]
    print(*b[i])
