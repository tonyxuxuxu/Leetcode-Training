"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowLength = len(grid[0])
        colLength = len(grid)

        for i in range(1, rowLength):
            grid[0][i] += grid[0][i-1]

        for j in range(1, colLength):
            grid[j][0] += grid[j-1][0]

        for i in range(1, rowLength):
            for j in range(1, colLength):
                grid[j][i] += min(grid[j-1][i], grid[j][i-1])

        return grid[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    input = [[1,3,1],
             [1,5,1],
             [4,2,1]]
    print(sol.minPathSum(input))