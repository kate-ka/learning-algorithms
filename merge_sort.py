def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)/2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]

                i += 1
            else:
                alist[k] = righthalf[j]

                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


alist = [54,26,93,17]
mergeSort(alist)
print(alist)


def another_mergesort(alist):

    if len(alist) == 1:
        return alist

    mid = len(alist)/2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]

    lefthalf = another_mergesort(lefthalf)
    righthalf = another_mergesort(righthalf)

    sortedl = []

    while lefthalf and righthalf:
        if lefthalf[0] > righthalf[0]:
            sortedl.append(righthalf.pop(0))
        else:
            sortedl.append(lefthalf.pop(0))

    sortedl += lefthalf
    sortedl += righthalf

    return sortedl


print (another_mergesort([54,26,93,17, 1, 3, 55]))