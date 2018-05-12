def search_min(tr, vizited):
    min = max(tr)
    for ind in vizited:
        for index, elem in enumerate(tr[ind]):
            if elem > 0 and elem < min and index not in vizited:
                min = elem
                index2 = index
    return min, index2


def prim(matr):
    toVisit = [i for i in range(1, len(matr))]
    vizited = [0]
    result = [0]
    for index in toVisit:
        weight, ind = search_min(matr, vizited)
        result.append(weight)
        vizited.append(ind)
    return result


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    matrix = [0] * n
    for i in range(n):
        matrix[i] = [0] * n
    for _ in range(m):
        x, y = tuple(map(int, input().split()))
        matrix[x][y] = matrix[y][x] = 1
    print(prim(matrix))
