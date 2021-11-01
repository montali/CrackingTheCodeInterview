def rotate(a):
    max = int(len(a) / 2) if len(a) % 2 == 0 else int(len(a) / 2) + 1
    length = len(a) - 1
    for i in range(max):
        for switch_x, switch_y in [
            (i, length - i),
            (length - i, length - i),
            (length - i, i),
        ]:
            temp = a[switch_x][switch_y]
            a[switch_x][switch_y] = a[i][i]
            a[i][i] = temp
    return a


test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(test_list))
