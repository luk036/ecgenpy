def BRGC_gen(n: int):
    """Binary Reflected Gray Code

    Args:
        n (int): [description]

    Yields:
        [type]: [description]
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
    """
    lst = list(0 for _ in range(n))
    yield lst
    for i in BRGC_gen(len(lst)):
        lst[i] = 1 - lst[i]  # flip
        yield lst


if __name__ == "__main__":
    s = "◾◽"
    print(" 0 1 2 3")
    for lst in BRGC(4):
        mylst = list(s[i] for i in lst)
        print("".join(mylst))
