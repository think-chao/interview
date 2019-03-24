# coding:utf-8
# @Filename:  Longest Palindromic Substring
# @Data:      2019-03-2019/3/24 09:49
# @Author:    Wangchao
# @Function:  最长回文子字符串
# 'aabaacaabaadcr' -- >  'aabaacaabaa'

def Manacher(s):
    if len(s) <= 1:
        return s
    s = '%' + '#'.join(s) + '#'
    half = [0] * len(s)  # 存放各个位置最大的半径
    right, mid, max_half = 0, 0, 0  # right， left存放出现最大半径的时候左右端点的位置
    for i in range(len(s)):
        if i < right:
            half[i] = min(half[2 * mid - i], right - i)
        else:
            half[i] = 1
        while i - half[i] >= 0 and i + half[i] < len(s) and s[i - half[i]] == s[i + half[i]]:
            half[i] += 1
        if right < i + half[i] - 1:
            right = i + half[i] - 1
            mid = i
        if half[i] > max_half:
            max_half = half[i]
            res = s[i - half[i] + 1:i + half[i]]
    return res.replace('#', '')


if __name__ == '__main__':
    print(Manacher('ssassbcssasse'))
