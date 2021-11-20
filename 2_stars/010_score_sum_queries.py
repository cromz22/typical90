def naive_solver(l, r):
    cls1_sum = 0
    cls2_sum = 0
    for i in range(l - 1, r):
        if cls[i] == 1:
            cls1_sum += points[i]
        elif cls[i] == 2:
            cls2_sum += points[i]
    print(cls1_sum, cls2_sum)


# plan
# 1. memoize accumulative sum
# 2. subtract
def memo(N, cls, points):
    cls1_acc = [0]
    cls2_acc = [0]
    cls1_sum = 0
    cls2_sum = 0
    for i in range(N):
        if cls[i] == 1:
            cls1_sum += points[i]
        elif cls[i] == 2:
            cls2_sum += points[i]
        cls1_acc.append(cls1_sum)
        cls2_acc.append(cls2_sum)

    return cls1_acc, cls2_acc


if __name__ == "__main__":
    N = int(input())
    cp = [map(int, input().split()) for _ in range(N)]
    cls, points = [list(i) for i in zip(*cp)]

    Q = int(input())
    lr = [map(int, input().split()) for _ in range(Q)]
    l, r = [list(i) for i in zip(*lr)]

    cls1_acc, cls2_acc = memo(N, cls, points)

    for q in range(Q):
        # naive_solver(l[q], r[q])
        left = max(l[q] - 1, 0)
        right = r[q]
        print(cls1_acc[right] - cls1_acc[left], cls2_acc[right] - cls2_acc[left])
