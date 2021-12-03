from math import log2


a, b, c = map(int, input().split())

# if log2(a) < b * log2(c):
#     print("Yes")
# else:
#     print("No")

if a < c ** b:
    print("Yes")
else:
    print("No")
