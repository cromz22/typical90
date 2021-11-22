n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum_a = sum(a)
sum_b = sum(b)

if (sum_a - sum_b) % 2 != k % 2:
    print("No")
elif abs(sum_a - sum_b) > k:
    print("No")
else:
    diff = 0
    for i in range(n):
        diff += abs(a[i] - b[i])
    if diff > k:
        print("No")
    else:
        print("Yes")
