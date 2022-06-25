""" Steinhaus-Johnson-Trotter algorithm """


def SJT_gen(n: int):
    """Generate the swaps for the Steinhaus-Johnson-Trotter algorithm.

    Args:
        n (int): [description]

    Returns:
        [type]: [description]

    Yields:
        [type]: [description]

    Examples:
        >>> for i in SJT_gen(4):
        ...     print("swap {} and {}".format(i, i + 1))
        ...
        swap 2 and 3
        swap 1 and 2
        swap 0 and 1
        swap 2 and 3
        swap 0 and 1
        swap 1 and 2
        swap 2 and 3
        swap 0 and 1
        swap 2 and 3
        swap 1 and 2
        swap 0 and 1
        swap 2 and 3
        swap 0 and 1
        swap 1 and 2
        swap 2 and 3
        swap 0 and 1
        swap 2 and 3
        swap 1 and 2
        swap 0 and 1
        swap 2 and 3
        swap 0 and 1
        swap 1 and 2
        swap 2 and 3
        swap 0 and 1
    """

    if n == 2:
        yield 0
        yield 0  # tricky part: return to the origin
        return

    gen = SJT_gen(n - 1)
    for x in gen:
        for i in range(n - 2, -1, -1):  # downward
            yield i
        yield x + 1
        for i in range(n - 1):  # upward
            yield i
        yield next(gen)  # tricky part


def SJT(n: int):
    """Generate the swaps for the Steinhaus-Johnson-Trotter algorithm.

    Args:
        n (int): [description]

    Returns:
        [type]: [description]

    Yields:
        [type]: [description]

    Examples:
        >>> fruits = list("🍉🍌🍇🍏")
        >>> for lst in SJT(4):
        ...     mylst = list(fruits[i] for i in lst)
        ...     print("".join(mylst))
        ...
        🍉🍌🍇🍏
        🍉🍌🍏🍇
        🍉🍏🍌🍇
        🍏🍉🍌🍇
        🍏🍉🍇🍌
        🍉🍏🍇🍌
        🍉🍇🍏🍌
        🍉🍇🍌🍏
        🍇🍉🍌🍏
        🍇🍉🍏🍌
        🍇🍏🍉🍌
        🍏🍇🍉🍌
        🍏🍇🍌🍉
        🍇🍏🍌🍉
        🍇🍌🍏🍉
        🍇🍌🍉🍏
        🍌🍇🍉🍏
        🍌🍇🍏🍉
        🍌🍏🍇🍉
        🍏🍌🍇🍉
        🍏🍌🍉🍇
        🍌🍏🍉🍇
        🍌🍉🍏🍇
        🍌🍉🍇🍏
    """
    perm = list(range(n))
    for x in SJT_gen(n):
        yield perm
        perm[x], perm[x + 1] = perm[x + 1], perm[x]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
