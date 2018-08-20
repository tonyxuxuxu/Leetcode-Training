"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0 for _ in range(n+1)]
        result[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                result[i] += result[j]*result[i-j-1]
        return result[n]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numTrees(3))