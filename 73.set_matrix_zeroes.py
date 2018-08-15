"""

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rowHasZero = False
        colHasZero = False
        row = len(matrix[0])
        col = len(matrix)

        for i in range(row):
            if matrix[0][i] == 0:
                rowHasZero = True

        for j in range(col):
            if matrix[j][0] == 0:
                colHasZero = True

        for i in range(1, row):
            for j in range(1, col):
                if matrix[j][i] == 0:
                    matrix[j][0] = matrix[0][i] = 0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[j][0] == 0 or matrix[0][i] == 0:
                    matrix[j][i] = 0

        if rowHasZero:
            for i in range(row):
                matrix[0][i] = 0

        if colHasZero:
            for j in range(col):
                matrix[j][0] = 0

        return matrix

if __name__ == '__main__':
    sol = Solution()
    input =[[1,1,1],
            [1,0,1],
            [1,1,1]]
    print(sol.setZeroes(input))
