n = int(input())
a, b, c = map(int, input().split())

# ub_x = n // a
# ub_y = n // b
# ub_z = n // c
# 
# ub_k = ub_x + ub_y + ub_z

# ans = ub_k
# for x in range(ub_x):
#     for y in range(ub_y):

ans = 10**9
for x in range(10**4):
    for y in range(10**4):
        z = n - a*x - b*y
        if z % c == 0 and z >= 0:
            k = x + y + z // c
            if k < ans:
                ans = k

print(ans)
