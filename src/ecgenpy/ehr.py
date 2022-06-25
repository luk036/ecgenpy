def Ehr_gen(n: int):
    """[summary]

    Args:
        n (int): [description]

    Yields:
        [type]: [description]

    Examples:
        >>> for i in Ehr_gen(4):
        ...     print("swap 0 and {}".format(i))
        ...
        swap 0 and 1
        swap 0 and 2
        swap 0 and 1
        swap 0 and 2
        swap 0 and 1
        swap 0 and 3
        swap 0 and 2
        swap 0 and 1
        swap 0 and 2
        swap 0 and 1
        swap 0 and 2
        swap 0 and 3
        swap 0 and 1
        swap 0 and 2
        swap 0 and 1
        swap 0 and 2
        swap 0 and 1
        swap 0 and 3
        swap 0 and 2
        swap 0 and 1
        swap 0 and 2
        swap 0 and 1
        swap 0 and 2
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
        b[1:k] = b[k-1:0:-1]


def Ehr(n: int):
    """[summary]

    Args:
        n (int): [description]

    Yields:
        list: [description]

    Examples:
        >>> fruits = list("🍉🍌🍇🍏")
        >>> for lst in Ehr(4):
        ...     mylst = list(fruits[i] for i in lst)
        ...     print("".join(mylst))
        ...
        🍉🍌🍇🍏
        🍌🍉🍇🍏
        🍇🍉🍌🍏
        🍉🍇🍌🍏
        🍌🍇🍉🍏
        🍇🍌🍉🍏
        🍏🍌🍉🍇
        🍉🍌🍏🍇
        🍌🍉🍏🍇
        🍏🍉🍌🍇
        🍉🍏🍌🍇
        🍌🍏🍉🍇
        🍇🍏🍉🍌
        🍏🍇🍉🍌
        🍉🍇🍏🍌
        🍇🍉🍏🍌
        🍏🍉🍇🍌
        🍉🍏🍇🍌
        🍌🍏🍇🍉
        🍇🍏🍌🍉
        🍏🍇🍌🍉
        🍌🍇🍏🍉
        🍇🍌🍏🍉
    """
    perm = list(range(n))
    for x in Ehr_gen(n):
        yield perm
        perm[0], perm[x] = perm[x], perm[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
