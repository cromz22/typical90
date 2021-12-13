import math


def prime_factorize(n):
    """
    https://en.wikipedia.org/wiki/Trial_division
    """
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def main():
    n = int(input())
    len_n = len(prime_factorize(n))

    print(math.ceil(math.log2(len_n)))


if __name__ == "__main__":
    main()
