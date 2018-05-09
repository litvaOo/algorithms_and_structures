def heap_sort (sequence):

    def sift_down (parent, limit):
        item = sequence[parent]
        while True:
            child = (parent << 1) + 1
            if child >= limit:
                break
            if child + 1 < limit and sequence[child] < sequence[child + 1]:
                child += 1
            if item < sequence[child]:
                sequence[parent] = sequence[child]
                parent = child
            else:
                break
        sequence[parent] = item

    length = len(sequence)
    for index in range((length >> 1) - 1, -1, -1):
        sift_down(index, length)
    for index in range(length - 1, 0, -1):
        sequence[0], sequence[index] = sequence[index], sequence[0]
        sift_down(0, index)
    return sequence


def binary_search(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    midpoint = 0
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found, midpoint


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    n_list = []
    m_list = []
    for _ in range(n):
        n_list.append(int(input()))
    for _ in range(m):
        m_list.append(int(input()))
    sorted_list = heap_sort(n_list)
    print(sorted_list)
    list_of_searches = [binary_search(sorted_list, item) for item in m_list]
    print([item[1]+1 for item in list_of_searches if item[0]])
