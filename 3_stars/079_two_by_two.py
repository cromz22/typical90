h, w = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

counter = 0
for j in range(w - 1):
    for i in range(h - 1):
        diff = b[i][j] - a[i][j]
        if diff != 0:
            a[i][j] += diff
            a[i + 1][j] += diff
            a[i][j + 1] += diff
            a[i + 1][j + 1] += diff
            counter += abs(diff)

flag = True
for i in range(h):
    if a[i][w - 1] != b[i][w - 1]:
        flag = False
for j in range(w):
    if a[h - 1][j] != b[h - 1][j]:
        flag = False

if flag == True:
    print("Yes")
    print(counter)
else:
    print("No")
