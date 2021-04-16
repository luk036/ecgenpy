def gray_code_gen(n):
    if n == 0:
        return
    yield from gray_code_gen(n - 1)
    yield n - 1
    yield from gray_code_gen(n - 1)


if __name__ == "__main__":
    lst = list("◾◾◾◾")
    print("".join(lst[::-1]))
    for i in gray_code_gen(4):
        lst[i] = "◽" if lst[i] == "◾" else "◾"  # flip
        print("{}: {}".format("".join(lst[::-1]), i))
