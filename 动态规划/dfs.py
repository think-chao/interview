# coding:utf-8
# @Filename:  dfs
# @Data:      2019-03-2019/3/24 21:53
# @Author:    Wangchao
# @Function:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

    def dfs(self, root):
        if root == None:
            return 0, 0
        leftLoot = self.dfs(root.left)
        rightLoot = self.dfs(root.right)
        lootIfRobbed = root.val + leftLoot[1] + rightLoot[1]
        lootIfNotRobbed = max(leftLoot[0], leftLoot[1]) + max(rightLoot[0], rightLoot[1])
        return lootIfRobbed, lootIfNotRobbed

    def robber(self, root):
        loot = self.dfs(root)
        return max(loot[0], loot[1])
