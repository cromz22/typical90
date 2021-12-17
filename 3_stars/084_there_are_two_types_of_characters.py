from itertools import combinations


n = int(input())
s = input()

if "o" in s and "x" in s:
    # naive idea
    # combi = list(combinations(range(n), 2))
    # counter = 0
    # for c in combi:
    #     substr = s[c[0] : c[1] + 1]
    #     if "o" in substr and "x" in substr:
    #         counter += 1
    # print(counter)

    # con
    # if an interval meets the requirements,
    # intervals that include it as a sub-interval
    # should also meet the requirements

    a = [0] * (n + 1)
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] == "o":
            a[i] = i
            b[i] = b[i - 1]
        elif s[i - 1] == "x":
            a[i] = a[i - 1]
            b[i] = i

    z = 0
    for r in range(1, n + 1):
        z += min(a[r], b[r])
    print(z)

else:
    print(0)
