N, Q = map(int, input().split())
a = list(map(int, input().split()))

# b = [0] * (N - 1)
#
# initial_difficulty = 0
# for i in range(N - 1):
#     b[i] = a[i] - a[i + 1]
#     initial_difficulty += abs(b[i])
b = [a[i + 1] - a[i] for i in range(N - 1)]
difficulty = sum(abs(elem) for elem in b)

# difficulty = initial_difficulty
for i in range(Q):
    l, r, v = map(int, input().split())
    # absv = abs(v)
    # if l == 1 and r == N:
    #     pass
    # elif l == 1:
    #     difficulty += absv
    # elif r == N:
    #     difficulty += absv
    # else:
    #     pass
    #     # difficulty += absv * 2
    # print(difficulty)

    if l > 1:
        difficulty -= abs(b[l - 2])
        b[l - 2] += v
        difficulty += abs(b[l - 2])
    if r < N:
        difficulty -= abs(b[r - 1])
        b[r - 1] -= v
        difficulty += abs(b[r - 1])
    print(difficulty)
