import numpy as np


T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = [int(input()) for _ in range(Q)]

theta = np.array(E) * 2 * np.pi / T

numerator = np.sqrt(X ** 2 + (Y + L * np.sin(theta) / 2) ** 2)
denominator = L * (1 - np.cos(theta)) / 2

# phi = np.arctan(numerator / denominator)
phi = np.degrees(np.arctan2(denominator, numerator))

for p in phi:
    print(p)
