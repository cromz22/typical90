from functools import reduce
import math


def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    abc_gcd = my_gcd(a, b, c)

    if abc_gcd == 1:
        div = a + b + c - 3
    else:
        div_a = a / abc_gcd - 1
        div_b = b / abc_gcd - 1
        div_c = c / abc_gcd - 1

        div = int(div_a + div_b + div_c)
    print(div)
