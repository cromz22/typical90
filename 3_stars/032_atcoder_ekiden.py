from itertools import permutations


def cats_and_dogs(v, cd_grid):
    for i in range(len(v) - 1):
        if cd_grid[v[i]][v[i + 1]]:
            return True
    return False


def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    if m == 0:
        min_val = 10 ** 18
        val = -1
        for v in permutations(range(n), n):
            val = 0
            for i, row in enumerate(a):
                val += row[v[i]]
            min_val = min(min_val, val)
        print(min_val)

    else:
        cats_and_dogs_list = [list(map(int, input().split())) for _ in range(m)]
        cats_and_dogs_grid = [[False] * n for _ in range(n)]
        for i in range(m):
            cats_and_dogs_grid[cats_and_dogs_list[i][0] - 1][
                cats_and_dogs_list[i][1] - 1
            ] = True
            cats_and_dogs_grid[cats_and_dogs_list[i][1] - 1][
                cats_and_dogs_list[i][0] - 1
            ] = True

        print(cats_and_dogs_grid)

        min_val = 10 ** 18
        val = -1
        for v in permutations(range(n), n):
            # if the combination is not possible
            if cats_and_dogs(v, cats_and_dogs_grid):
                continue
            else:
                val = 0
                for i, row in enumerate(a):
                    val += row[v[i]]
                min_val = min(min_val, val)

        if val == -1:
            print("-1")
        else:
            print(min_val)


if __name__ == "__main__":
    main()
