n, q = map(int, input().split())
a = list(map(int, input().split()))

shift = 0
for i in range(q):
    t, x, y = map(int, input().split())
    x = x - 1
    y = y - 1

    x = (x - shift) % n
    y = (y - shift) % n

    if t == 1:
        a[x], a[y] = a[y], a[x]
    elif t == 2:
        shift = (shift + 1) % n
    else:
        print(a[x])
