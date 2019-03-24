# coding:utf-8
# @Filename:  mergeSort
# @Data:      2019-03-2019/3/24 21:59
# @Author:    Wangchao
# @Function:  

def merge(left, right):
    result = []
    l, r = 0, 0
    while l<len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left, right = mergeSort(nums[:mid]), mergeSort(nums[mid:])
    return merge(left, right)