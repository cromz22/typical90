N, L = map(int, input().split())

# naive idea
# e.g. n = 17, l = 3
# n % l = 5 -> permutation of 3 3 3 3 3 1 1
# and 3 3 3 3  1 1 1  1 1
# and 3 3 3  1 1 1  1 1 1  1 1
# and ...

# DP
if N == L:
    print(2)
elif N < L:
    print(1)
else:
    dp = [0] * (N + 1)  # dp[i]: how many ways there are to get to the i-th step
    dp[0] = 1
    for i in range(1, L):
        dp[i] = dp[i - 1]
    for i in range(L, N + 1):
        dp[i] = dp[i - 1] + dp[i - L]

    print(dp[N] % 1000000007)
