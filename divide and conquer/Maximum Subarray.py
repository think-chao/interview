#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:wchao118
@license: Apache Licence 
@file: Maximum Subarray.py 
@time: 2019/03/28
@contact: wchao118@gmail.com
@software: PyCharm 
"""

"""
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


def find_max_cross_subarray(start, mid, end, nums):
    """
    :param start:
    :param mid:
    :param end:
    :param nums:
    :return:
    如果最長子數組跨越了中心點，那麼久可以將i,mid和mid, j組成的最大子數組拼接起來就可以
    """
    max_left, max_right = -1, -1
    left_sum, right_sum = -100, -100
    sum = 0
    for i in range(mid, start - 1, -1):
        sum += nums[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    sum = 0
    for j in range(mid + 1, end + 1):
        sum += nums[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum


def divide_and_conquer(start, end, nums):
    if start == end:
        return start, end, nums[start]
    mid = (start + end) // 2
    left_start, left_end, left_sum = divide_and_conquer(start, mid, nums)
    right_start, right_end, right_sum = divide_and_conquer(mid + 1, end, nums)
    cross_start, cross_end, cross_sum = find_max_cross_subarray(start, mid, end, nums)
    if left_sum > right_sum and left_sum > cross_sum:
        return left_start, left_end, left_sum
    elif right_sum > left_sum and right_sum > cross_sum:
        return right_start, right_end, right_sum
    else:
        return cross_start, cross_end, cross_sum


if __name__ == '__main__':
    so = Solution()
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(so.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(divide_and_conquer(0, len(A)-1, A))
