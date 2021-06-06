def Ehr_gen(n: int):
    """[summary]

    Args:
        n (int): [description]

    Yields:
        [type]: [description]
    """
    b = list(range(n))  # b[0] is never used
    c = [0] * (n + 1)  # c[0] is never used
    while True:
        k = 1
        while True:
            if c[k] == k:
                c[k] = 0
                k += 1
            if c[k] < k:
                break
        if k == n:
            break
        c[k] += 1
        yield b[k]
        b[1:k] = b[k - 1 : 0 : -1]


def Ehr(perm: list):
    """[summary]

    Args:
        perm (list): [description]

    Yields:
        list: [description]
    """
    n = len(perm)
    for k in Ehr_gen(n):
        yield perm
        perm[0], perm[k] = perm[k], perm[0]
    yield perm


if __name__ == "__main__":
    fruits = list("🍉🍌🍇🍏🍍")
    print(" 0 1 2 3 4")
    # print("".join(perm))
    for perm in Ehr(fruits):
        print("".join(perm))
