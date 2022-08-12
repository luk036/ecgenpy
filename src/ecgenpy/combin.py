""" Combinations """
from functools import lru_cache


@lru_cache
def comb(n: int, k: int) -> int:
    """Number of combination

    Args:
        n (int): [description]
        k (int): [description]

    Returns:
        int: [description]

    Examples:
        >>> comb(6, 3)
        20
    """
    if k >= n or k == 0:
        return 1
    return comb(n - 1, k - 1) + comb(n - 1, k)


def EMK_gen(n: int, k: int):
    """[summary]

    Args:
        n (int): [description]
        k (int): [description]

    Yields:
        Iterator[(int, int)]: [description]

    Examples:
        >>> for x, y in EMK_gen(6, 3):
        ...     print(f"swap {x} and {y}")
        ...
        swap 2 and 3
        swap 1 and 2
        swap 0 and 1
        swap 3 and 4
        swap 1 and 0
        swap 2 and 1
        swap 1 and 3
        swap 0 and 1
        swap 1 and 2
        swap 4 and 5
        swap 2 and 0
        swap 0 and 1
        swap 3 and 2
        swap 1 and 0
        swap 2 and 1
        swap 1 and 4
        swap 0 and 1
        swap 1 and 2
        swap 2 and 3
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
    """EMK

    Args:
        n ([type]): [description]
        k ([type]): [description]
        Zero (int, optional): [description]. Defaults to 0.
        One (int, optional): [description]. Defaults to 1.

    Yields:
        [type]: [description]

    Examples:
        >>> for s in EMK(6, 3, Zero="◾", One="◽"):
        ...     print("".join(s))
        ...
        ◽◽◽◾◾◾
        ◽◽◾◽◾◾
        ◽◾◽◽◾◾
        ◾◽◽◽◾◾
        ◾◽◽◾◽◾
        ◽◾◽◾◽◾
        ◽◽◾◾◽◾
        ◽◾◾◽◽◾
        ◾◽◾◽◽◾
        ◾◾◽◽◽◾
        ◾◾◽◽◾◽
        ◽◾◾◽◾◽
        ◾◽◾◽◾◽
        ◾◽◽◾◾◽
        ◽◾◽◾◾◽
        ◽◽◾◾◾◽
        ◽◾◾◾◽◽
        ◾◽◾◾◽◽
        ◾◾◽◾◽◽
        ◾◾◾◽◽◽
    """
    s = [One] * k + [Zero] * (n - k)
    yield s
    for x, y in EMK_gen(n, k):
        s[x], s[y] = s[y], s[x]
        yield s


if __name__ == "__main__":
    import doctest

    doctest.testmod()
