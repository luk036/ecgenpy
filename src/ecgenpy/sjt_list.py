def SJT2(n):
    """Generate the swaps for the Steinhaus-Johnson-Trotter algorithm."""
    if n == 2:
        yield [0, 1]
        yield [1, 0]  # tricky part: return to the origin
        return

    gen = SJT2(n - 1)
    for pi in gen:
        for i in range(n - 1, -1, -1):  # downward
            yield pi[:i] + [n - 1] + pi[i:]
        pi = next(gen)
        for i in range(n):  # upward
            yield pi[:i] + [n - 1] + pi[i:]


if __name__ == "__main__":
    fruits = list("🍉🍌🍇🍏")
    print(" 0 1 2 3")
    # print("".join(perm))
    for perm in SJT2(fruits):
        print("".join(perm))
