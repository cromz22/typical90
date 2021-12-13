n, k = map(int, input().split())

C = 10**9 + 7

ans = -1
if k >= 2 and n >= 2:
    ans = k * (k-1) * pow(k-2, n-2, C)
elif n == 1:
    ans = k
elif k == 1:
    if n == 1:
        ans = 1
    else:
        ans = 0

print(ans % C)
