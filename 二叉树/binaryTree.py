# coding:utf-8
# @Filename:  binaryTree
# @Data:      2019-03-2019/3/24 11:07
# @Author:    Wangchao
# @Function:  前序遍历，中序遍历，递归非递归，层级遍历

import os


class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def preOder(self, node):
        if node is None:
            return node
        print(node.value)
        self.preOder(node.left)
        self.preOder(node.right)

    def preOderNoneRecursive(self, root):
        stack = []
        ret = []
        while stack or root:
            while root:
                ret.append(root.value)
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                root = t.right
        print(ret)
        return ret

    def InOderRecursive(self, root):
        ret, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                ret.append(t.value)
                root = t.right
        print(ret)

    def AfterOderRecursive(self, root):
        stack, flag, ret = [], [], []
        while root or stack:
            while root:
                stack.append(root)
                flag.append(0)
                root = root.left
            if stack:
                top = stack[-1]
                if top.right and not flag[-1]:
                    flag[-1] = 1
                    root = top.right
                else:
                    flag.pop()
                    ret.append(stack.pop().value)
        print(ret)
        return ret

    def LevelOder(self, root):
        stack = [root]
        ret = []
        while stack:
            current = stack.pop(0)
            ret.append(current.value)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return ret


if __name__ == '__main__':
    node = Node(3)
    node.left = Node(2)
    node.right = Node(4)
    node.left.left = Node(1)
    node.preOderNoneRecursive(node)
    node.InOderRecursive(node)
    node.AfterOderRecursive(node)
