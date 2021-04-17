def combin_gen(n, k):
    if n <= k or k == 0:
        return
    if k == 1:
        for i in range(n - 1):
            yield (i, i + 1)
    else:
        yield from combin_gen(n - 1, k)
        yield (n - 2, n - 1)
        yield from combin_neg(n - 2, k - 1)
        yield (k - 2, n - 2)
        yield from combin_gen(n - 2, k - 2)


def combin_neg(n, k):
    if n <= k or k == 0:
        return
    if k == 1:
        for i in range(n - 1, 0, -1):
            yield (i, i - 1)
    else:
        yield from combin_neg(n - 2, k - 2)
        yield (n - 2, k - 2)
        yield from combin_gen(n - 2, k - 1)
        yield (n - 1, n - 2)
        yield from combin_neg(n - 1, k)


if __name__ == "__main__":
    s = list("◽◽◽◾◾◾")
    print("".join(s[::-1]))
    for x, y in combin_gen(6, 3):
        s[x], s[y] = s[y], s[x]
        print("{}: {}->{}".format("".join(s[::-1]), x, y))
