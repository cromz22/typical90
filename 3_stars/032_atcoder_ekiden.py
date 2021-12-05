from itertools import permutations


def cats_and_dogs(v, candd_grid):
    for i in range(len(v) - 1):
        if candd_grid[v[i]][v[i + 1]]:
            return True
    return False


def main():
    n = int(input())

    a = [list(map(int, input().split())) for _ in range(n)]
    # rows reperesent players, columns represent intervals

    m = int(input())

    if m == 0:
        min_val = 10 ** 18
        val = -1
        for v in permutations(range(n), n):
            val = 0
            for j in range(n):
                val += a[v[j]][j]
            min_val = min(min_val, val)
        print(min_val)

    else:
        candd_list = [list(map(int, input().split())) for _ in range(m)]
        # memoize pairs that are cats and dogs
        candd_grid = [[False] * n for _ in range(n)]
        for i in range(m):
            candd_grid[candd_list[i][0] - 1][candd_list[i][1] - 1] = True
            candd_grid[candd_list[i][1] - 1][candd_list[i][0] - 1] = True

        min_val = 10 ** 18
        val = -1
        for v in permutations(range(n)):
            # if the combination includes a cats-and-dogs pair, skip the combination
            if cats_and_dogs(v, candd_grid):
                continue
            else:
                val = 0
                for j in range(n):
                    val += a[v[j]][j]
                min_val = min(min_val, val)

        # if all the combinations are bad
        if min_val == 10 ** 18:
            print(-1)
        else:
            print(min_val)


if __name__ == "__main__":
    main()
