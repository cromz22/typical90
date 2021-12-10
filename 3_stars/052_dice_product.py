n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

C = 10 ** 9 + 7

ans = 1
for elem in a:
    ans *= sum(elem)
print(ans % C)
