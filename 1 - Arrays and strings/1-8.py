def crazy_function(a):
    rows = []
    cols = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for row in rows:
        for j in range(len(a[row])):
            a[row][j] = 0
    for col in cols:
        for j in range(len(a)):
            a[j][col] = 0
    return a


if __name__ == "__main__":
    print(crazy_function([[1, 2, 3], [4, 5, 6], [7, 0, 9]]))
