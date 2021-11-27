def base10_to_9(num):
    nine_number = ""
    while num > 0:
        nine_number += str(num % 9)
        num //= 9
    return int(nine_number[::-1])


def operation(n):
    # convert n to base 10
    base10_n = int(n, 8)

    # then convert to base 9
    base9_n = base10_to_9(base10_n)

    # convert str 8 to str 5
    base8_n = str(base9_n).replace("8", "5")

    return base8_n


if __name__ == "__main__":
    n, k = input().split()
    k = int(k)
    # n is base 8 string

    if n == "0":
        exit(print(0))

    for i in range(k):
        n = operation(n)

    print(n)
