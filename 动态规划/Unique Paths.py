#coding=utf-8
"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1]*m for _ in range(n)]
        for i in range(1, n):
        	for j in range(1, m):
        		dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[-1][-1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        col, row = len(obstacleGrid[0]),len(obstacleGrid)
        for i in range(row):
        	for j in range(col):
        		if obstacleGrid[i][j] == 1:
        			index_x, index_y = i, j
        dp = [[1]*col for _ in range(row)]
        if index_x == 0:
        	dp[index_x][index_y:] = 0
        elif index_y == 0:
        	dp[index_x][index_y:] = 0
        else:
        	dp[index_x][index_y] = 0
        for i in range(1, row):
        	for j in range(1, col):
        		dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
        print(dp)
        return dp[-1][-1]



if __name__ == '__main__':
	print(Solution().uniquePaths(7, 3))
	print(Solution().uniquePathsWithObstacles([
		[0, 0, 0],
		[0, 1, 0],
		[0, 0, 0]]))