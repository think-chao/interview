# coding:utf-8
# @Filename:  houseRobber
# @Data:      2019-03-2019/3/24 10:09
# @Author:    Wangchao
# @Function:  类似01背包

# it will automatically contact the police if two adjacent houses were broken into on the same night.
"""
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

转移方程  dp[i] = max(dp[i-1] ,dp[i-2]+v[i])
"""


def houseRobber(value):
    dp = [0] * (len(value) + 1)
    dp[1], dp[2] = value[0], max(value[0], value[1])
    for i in range(3, len(value)+1):
        dp[i] = max(dp[i-1], dp[i-2]+value[i-1])
    print(dp[-1])


if __name__ == '__main__':
    houseRobber([1, 2, 3, 1])

