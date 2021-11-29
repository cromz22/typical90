from bisect import bisect


n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]

a.sort()

for student_rate in b:
    index = bisect(a, student_rate)
    if index == 0:
        print(a[index] - student_rate)
    elif index == n:
        print(student_rate - a[index - 1])
    else:
        print(min(a[index] - student_rate, student_rate - a[index - 1]))
