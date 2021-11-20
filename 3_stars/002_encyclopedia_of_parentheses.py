from itertools import product

# Naive idea
# 1. Generate random strings composed of "(" and ")" whose lengths are N
# 2. For each string, check if it is valid (use depth)
def is_valid(string: str):
    depth = 0
    for s in string:
        if s == "(":
            depth += 1
        elif s == ")":
            depth -= 1
            if depth < 0:
                break
        else:
            print("invalid string")
            exit(1)

    if depth == 0:
        return True
    return False


if __name__ == "__main__":
    N = int(input())
    if N % 2 == 1:
        exit(0)

    for candidate in product(["(", ")"], repeat=N):
        candidate_str = "".join(candidate)
        if (is_valid(candidate_str)):
            print(candidate_str)


# Another idea
# Incrementally generate valid strings

# LEFT = "("
# RIGHT = ")"
# 
# valid_strings = {}
# if N % 2 == 0:
#     print()
# elif N == 2:
#     valid_strings["2"] = [LEFT + RIGHT]
# elif N == 4:
#     valid_strings["4"] = []
#     for elem in valid_strings["2"]:
#         valid_strings["4"].append(LEFT + elem + RIGHT)
#         # also () + elem, elem + (), etc.
