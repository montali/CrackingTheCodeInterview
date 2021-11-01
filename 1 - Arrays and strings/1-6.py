def compress_noinplace(a):
    comp = ""
    i = 0
    while i < len(a):
        char = a[i]
        count = 0
        while i < len(a) and a[i] == char:
            count += 1
            i += 1
        comp += char + str(count)
    return comp


def compress_inplace(a):
    i = 0
    a = list(a)
    while i < len(a):
        char = a[i]
        count = 0
        while a[i] == char:
            if count > 0:
                a.pop(i + 1)
            count += 1
        a.insert(i, str(count))
        i += 2
    return str(a)


if __name__ == "__main__":
    a = input()
    print(compress_noinplace(a))
    print(compress_inplace(a))
