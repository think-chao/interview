# coding:utf-8
# @Filename:  quickSort
# @Data:      2019-03-2019/3/24 21:54
# @Author:    Wangchao
# @Function:  


"""
选取基值，将数值分布于基值两边，就成为有序
"""


def quickSort(nums):
    if len(nums) <= 1:
        return nums
    base = nums[0]
    left, right = [], []
    nums.remove(nums[0])
    for num in nums:
        if num < base:
            left.append(num)
        else:
            right.append(num)
    return quickSort(left) + [base] + quickSort(right)
