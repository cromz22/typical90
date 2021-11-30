n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

answer = 0
for i in range(n):
    answer += abs(a[i] - b[i])

print(answer)
