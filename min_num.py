# def find_min(list_of_numbs, k):
#     list_of_numbs.sort()
#     return list_of_numbs[k-1]
#
# print find_min( [5,6,3,7,8,2], 2)


def min_num(list_of_nums, k):
    for i in range(k):
        min_numb = list_of_nums[0]
        min_index = 0
        for index, item in enumerate(list_of_nums):
            if item <= min_numb:
                min_numb = item
                min_index = index

        del list_of_nums[min_index]

    return min_numb

print min_num( [5,6,3,7,8,2], 3)


