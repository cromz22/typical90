import numpy as np


n, k = map(int, input().split())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

# naive idea
# 1. generate possible combinations
# 2. calculate the score for each combination and get the max one

# sophisticated idea
# 1. consider how many points you can additionally get by half-solving/solving a problem
# 1. concat and sort
# 1. sum top k elements

a = np.array(a)
b = np.array(b)
con = np.concatenate([a-b, b])
con.sort()
ans = con[-k:].sum()
print(ans)
