# coding:utf-8
# @Filename:  pack
# @Data:      2019-03- 09:27
# @Author:    Wangchao
# @Function:  背包问题

# ==============================================================================
# 1. Given n items with size Ai, an integer m denotes the size of a backpack.
#    How full you can fill this backpack?
# [2,3,5,7],11 --->10
# [2,3,5,7],12 --->12


def pack_one(weights, size):
    """
    :param weights: n items with size weights[i]
    :param size:    how many weight can the pack holds
    :return:        the max value
    """
    # dp[i][j] 表示背包容量为j的时候，前i个物品能达到的最大重量
    #
    dp = [[0] * (size + 1) for _ in range(len(weights)+1)]
    for i in range(1, len(weights) + 1):
        for j in range(1, size + 1):
            # 如果当前放不下
            if j < weights[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - weights[i - 1]] + weights[i - 1], dp[i - 1][j])
    return dp[-1][-1]


def pack_one_upgrade(weights, size):
    """
    :param weights:
    :param size:
    :return:
    """
    # dp[j]表示背包空间为j的时候能装的物品的最大容量
    # 数组维度下降要求 在求dp[j]的时候, dp[j-weights[i]]是没有变过的
    dp = [0 for _ in range(size + 1)]
    for i in range(1, len(weights) + 1):
        for j in range(size, weights[i-1]-1, -1):
            dp[j] = max(dp[j], dp[j - weights[i-1]] + weights[i-1])
    return dp[-1]


def pack_two(weights, value, max_size):
    """
    :param weights: [2, 3, 5, 7]
    :param value:   [1, 5, 2, 4]
    :param max_size: 10 ----> 15
    :return: 可以重复选择背包里的元素
    """
    dp = [0 for _ in range(max_size + 1)]
    for i in range(1, len(weights) + 1):
        for j in range(weights[i-1], max_size+1):
            dp[j] = max(dp[j-weights[i-1]]+value[i-1], dp[j])
    return dp[-1]


if __name__ == '__main__':
    print(pack_one([2, 5, 3, 7], 12))
    print(pack_one_upgrade([2, 5, 3, 7], 12))
    print(pack_two([2, 3, 5, 7], [1, 5, 2, 4], 10))
