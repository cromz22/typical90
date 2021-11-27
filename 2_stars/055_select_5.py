# import sys
# input = sys.stdin.readline

# n, p, q = map(int, input().strip().split())
# a = list(map(int, input().strip().split()))

n, p, q = map(int, input().split())
a = list(map(int, input().split()))

# Naive idea
# 1. Choose 5 integers out of the N integers and multiply them
# 2. Divide the product by P and calculate the residual
# 3. Compare the residual with Q

# import itertools
# # from functools import reduce
# # from operator import mul
#
# combs = list(itertools.combinations(a, 5))
# counter = 0
# for comb in combs:
#     # residual = reduce(mul, comb) % p
#     residual = comb[0] % p * comb[1] % p * comb[2] % p * comb[3] %p * comb[4] % p
#
#     if residual == q:
#         counter += 1
#
# print(counter)

# counter = 0
# for i in range(n):
#     for j in range(i):
#         for k in range(j):
#             for l in range(k):
#                 for m in range(l):
#                     residual = a[i] % p * a[j] % p * a[k] % p * a[l] % p * a[m] % p
#                     if residual == q:
#                         counter += 1
#
# print(counter)

# counter = 0
# for i in range(0, n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             for l in range(k+1, n):
#                 for m in range(l+1, n):
#                     residual = a[i] % p * a[j] % p * a[k] % p * a[l] % p * a[m] % p
#                     if residual == q:
#                         counter += 1
#
# print(counter)

# counter = 0
# for i in range(0, n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             for l in range(k+1, n):
#                 for m in range(l+1, n):
#                     residual = ((((a[i] % p) * a[j] % p) * a[k] % p) * a[l] % p) * a[m] % p
#                     if residual == q:
#                         counter += 1
#
# print(counter)

# counter = 0
# for i in range(0, n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             for l in range(k+1, n):
#                 for m in range(l+1, n):
#                     residual = ((((a[i] * a[j] % p) * a[k] % p) * a[l] % p) * a[m]) % p
#                     if residual == q:
#                         counter += 1
#
# print(counter)

from itertools import combinations

counter = 0
for a, b, c, d, e in combinations(a, 5):
    # if a % p * b % p * c % p * d % p * e % p == q:
    if (a * b * c * d * e) % p == q:
        counter += 1
print(counter)
