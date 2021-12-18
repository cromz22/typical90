def divide(m, diff):
    """
    Divide the yokan (`diff`) into `counter` pieces
    so that the length of the shortest piece is `m`, except for the last one
    """
    length = 0  # length of a piece
    counter = 0  # number of pieces
    for elem in diff:
        length += elem
        if length >= m:
            length = 0
            counter += 1

    return counter


def general_bisect(diff, k, l):
    """
    general bisect (https://qiita.com/drken/items/97e37dd6143e33a64c8c)
    """
    left = -1
    right = l + 1

    while right - left > 1:
        # start asking questions by checking if the middle value can be the answer
        middle = (right + left) // 2

        # this defines the general condition
        if (
            divide(middle, diff) >= k + 1
        ):  # which means you can widen the length candidate
            left = middle  # the answer is in the right half
        else:  # which means you need to shorten the candidate
            right = middle  # the answer is in the left half

    return left


def main():
    n, l = map(int, input().split())  # n+1: number of splits, l: total length of yokan
    k = int(input())  # you want to divide the yokan into k+1 pieces
    a = list(map(int, input().split()))
    a.append(l)

    diff = [a[0]]  # length of each pieces
    for i in range(n):
        diff.append(a[i + 1] - a[i])

    ans = general_bisect(diff, k, l)
    print(ans)


if __name__ == "__main__":
    main()
