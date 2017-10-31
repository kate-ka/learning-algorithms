from random import randrange
import time


def min_num(list_of_nums):
    min_numb = list_of_nums[0]
    for item in list_of_nums:
        if item <= min_numb:
            min_numb = item
    return min_numb


print min_num([1, 2, 3, 4, 0, 9, -1])


def minimal_num(list_of_nums):
    for item in list_of_nums:
        minimal = item
        for item_item in list_of_nums:
            if item_item <= minimal:
                minimal =item_item
    return minimal

print minimal_num([1, 2, 3, 4, 0, 9, -1])


for listSize in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print min_num(alist)
    end = time.time()
    print ("Size: %d time: %f" % (listSize, end - start))
