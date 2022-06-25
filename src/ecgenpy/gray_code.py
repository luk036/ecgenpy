def BRGC_gen(n: int):
    """Binary Reflected Gray Code

    Args:
        n (int): [description]

    Yields:
        [type]: [description]

    Examples:
        >>> for i in BRGC_gen(4):
        ...     print("flip {}".format(i))
        ...
        flip 0
        flip 1
        flip 0
        flip 2
        flip 0
        flip 1
        flip 0
        flip 3
        flip 0
        flip 1
        flip 0
        flip 2
        flip 0
        flip 1
        flip 0
    """
    if n == 1:
        yield 0
        return
    yield from BRGC_gen(n - 1)
    yield n - 1
    yield from BRGC_gen(n - 1)


def BRGC(n: int):
    """Binary Reflected Gray Code

    Args:
        n (int): [description]

    Yields:
        [type]: [description]

    Examples:
        >>> s = "◾◽"
        >>> for lst in BRGC(4):
        ...     mylst = list(s[i] for i in lst)
        ...     print("".join(mylst))
        ...
        ◾◾◾◾
        ◽◾◾◾
        ◽◽◾◾
        ◾◽◾◾
        ◾◽◽◾
        ◽◽◽◾
        ◽◾◽◾
        ◾◾◽◾
        ◾◾◽◽
        ◽◾◽◽
        ◽◽◽◽
        ◾◽◽◽
        ◾◽◾◽
        ◽◽◾◽
        ◽◾◾◽
        ◾◾◾◽
    """
    lst = list(0 for _ in range(n))
    yield lst
    for i in BRGC_gen(n):
        lst[i] = 1 - lst[i]  # flip
        yield lst


if __name__ == "__main__":
    import doctest

    doctest.testmod()
