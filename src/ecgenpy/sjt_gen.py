def sjt_gen(n):
    """Generate the swaps for the Steinhaus-Johnson-Trotter algorithm."""
    if n == 1:
        return

    down = True
    for x in sjt_gen(n - 1):
        if down:
            for i in range(n - 2, -1, -1):
                yield i
            yield x + 1
        else:  # up
            for i in range(n - 1):
                yield i
            yield x
        down = not down
    for i in range(n - 1):
        yield i


if __name__ == "__main__":
    perm = list("🍑🍉🍌🍇")
    print(" 0 1 2 3")
    print("".join(perm))
    for x in sjt_gen(4):
        perm[x], perm[x + 1] = perm[x + 1], perm[x]
        print("{}: {}<->{}".format("".join(perm), x, x + 1))
