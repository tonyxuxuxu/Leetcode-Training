"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if k == 0 or n < 1:
            return res

        self.dfs(n, k, [], res, 1)
        return res

    def dfs(self, n, k, path, res, index):
        length = len(path)
        # if len(path) == k:
        if length == k:
            res.append(path[:])
            return

        # TLE problem solved by adding this
        if k - length > n - index + 1:  # need k numbers in total , still need (k-lenth)
            return

        for num in range(index, n + 1):
            if num not in path:
                path += [num]
                self.dfs(n, k, path, res, num + 1)
                path.pop()