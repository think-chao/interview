# coding:utf-8
# @Filename:  heapSort
# @Data:      2019-03-2019/3/24 22:08
# @Author:    Wangchao
# @Function:

def construct(nums, start, end):
    root = start
    while 2 * root + 1 <= end:
        leftChild = 2 * root + 1
        if leftChild + 1 <= end and nums[leftChild] < nums[leftChild + 1]:
            leftChild += 1
        if nums[root] < nums[leftChild]:
            nums[root], nums[leftChild] = nums[leftChild], nums[root]
            root = leftChild
        else:
            break


def heapSort(nums):
    firstNoneLeaf = len(nums) // 2 - 1
    for i in range(firstNoneLeaf, -1, -1):
        construct(nums, i, len(nums) - 1)
    for end in range(len(nums) - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        construct(nums, 0, end - 1)
    return nums
