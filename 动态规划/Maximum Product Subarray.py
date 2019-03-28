#!/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:wchao118
@license: Apache Licence 
@file: Maximum Product Subarray.py 
@time: 2019/03/28
@contact: wchao118@gmail.com
@software: PyCharm 
"""

"""
Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n, n * big, n * small), min(n, n * big, n * small)
            maximum = max(maximum, big)
        return maximum

    def maxProduct1(self, nums):
        dp_max, dp_min = [0]*len(nums), [0]*len(nums)
        dp_max[0], dp_min[0], max_ret = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            dp_max[i], dp_min[i] = max(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i]), min(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i])
            max_ret = max(max_ret, dp_max[i])
        print(max_ret)
        return max_ret


if __name__ == '__main__':
    so = Solution()
    nums = [2, 3, -2, 4]
    so.maxProduct1(nums)
