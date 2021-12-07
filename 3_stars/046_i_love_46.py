from collections import Counter


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_residual_uniq = Counter([elem % 46 for elem in a])
b_residual_uniq = Counter([elem % 46 for elem in b])
c_residual_uniq = Counter([elem % 46 for elem in c])

counter = 0
for i, cnt_a in a_residual_uniq.items():
    for j, cnt_b in b_residual_uniq.items():
        for k, cnt_c in c_residual_uniq.items():
            if (i + j + k) % 46 == 0:
                counter += cnt_a * cnt_b * cnt_c

print(counter)
