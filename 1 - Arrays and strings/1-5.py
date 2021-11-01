def check(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    edits = 0
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                edits += 1
                if edits > 1:
                    return False
        return True
    else:
        a, b = (b, a) if len(a) < len(b) else (a, b)
        for i in range(len(a)):
            if a[i] != b[i - edits]:
                edits += 1
                if edits > 1:
                    return False
        return True


if __name__ == "__main__":
    a = input()
    b = input()
    print(check(a, b))
