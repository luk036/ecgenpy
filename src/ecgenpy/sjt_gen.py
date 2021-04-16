def PlainChanges(n):
    """Generate the swaps for the Steinhaus-Johnson-Trotter algorithm."""
    if n < 1:
        return
    up = range(n - 1)
    down = range(n - 2, -1, -1)
    recur = PlainChanges(n - 1)
    try:
        while True:
            for x in down:
                yield x
            yield next(recur) + 1
            for x in up:
                yield x
            yield next(recur)
    except StopIteration:
        pass


if __name__ == "__main__":
    perm = list("🍑🍉🍌🍇")
    print("".join(perm))
    for x in PlainChanges(4):
        perm[x], perm[x + 1] = perm[x + 1], perm[x]
        print("{}: {}<->{}".format("".join(perm), x, x + 1))
