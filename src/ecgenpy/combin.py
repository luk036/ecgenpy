""" Combinations """


def EMK_gen(n: int, k: int):
    """[summary]

    Args:
        n (int): [description]
        k (int): [description]

    Yields:
        Iterator[(int, int)]: [description]
    """
    if n <= k or k == 0:
        return
    if k == 1:
        for i in range(n - 1):
            yield (i, i + 1)
    else:
        yield from EMK_gen(n - 1, k)
        yield (n - 2, n - 1)
        yield from EMK_neg(n - 2, k - 1)
        yield (k - 2, n - 2)
        yield from EMK_gen(n - 2, k - 2)


def EMK_neg(n: int, k: int):
    """[summary]

    Args:
        n (int): [description]
        k (int): [description]

    Yields:
        [type]: [description]
    """
    if n <= k or k == 0:
        return
    if k == 1:
        for i in range(n - 1, 0, -1):
            yield (i, i - 1)
    else:
        yield from EMK_neg(n - 2, k - 2)
        yield (n - 2, k - 2)
        yield from EMK_gen(n - 2, k - 1)
        yield (n - 1, n - 2)
        yield from EMK_neg(n - 1, k)


def EMK(n: int, k: int, Zero=0, One=1):
    """[summary]

    Args:
        n ([type]): [description]
        k ([type]): [description]
        Zero (int, optional): [description]. Defaults to 0.
        One (int, optional): [description]. Defaults to 1.

    Yields:
        [type]: [description]
    """
    s = [One] * k + [Zero] * (n - k)
    yield s
    for x, y in EMK_gen(n, k):
        s[x], s[y] = s[y], s[x]
        yield s


if __name__ == "__main__":
    print(" 0 1 2 3 4 5")
    for s in EMK(6, 3, Zero="◾", One="◽"):
        print("".join(s))
