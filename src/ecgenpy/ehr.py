def Ehr_gen(n: int):
    """[summary]

    Args:
        n (int): [description]

    Yields:
        [type]: [description]

    Examples:
        >>> fruits = list("🍉🍌🍇🍏")
        >>> n = len(fruits)
        >>> perm = list(range(n))
        >>> for x in Ehr_gen(n):
        ...     mylst = list(fruits[i] for i in perm)
        ...     print("".join(mylst))
        ...     perm[0], perm[x] = perm[x], perm[0]
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

    Examples:
        >>> fruits = list("🍉🍌🍇🍏")
        >>> for lst in Ehr(4):
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
    n = len(perm)
    for k in Ehr_gen(n):
        yield perm
        perm[0], perm[k] = perm[k], perm[0]
    yield perm


if __name__ == "__main__":
    import doctest

    doctest.testmod()
