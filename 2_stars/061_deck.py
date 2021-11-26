from collections import deque


q = int(input())
tx = [map(int, input().split()) for _ in range(q)]
t, x = [list(i) for i in zip(*tx)]


d = deque([])
for i in range(q):
    if t[i] == 1:
        d.appendleft(x[i])
    elif t[i] == 2:
        d.append(x[i])
    else:
        print(d[x[i] - 1])
