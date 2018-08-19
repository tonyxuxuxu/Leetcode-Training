"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        res.append(path)
        for i in range(index, len(nums)):
            if nums[i] == nums[i-1] and i > index:
                continue
            self.dfs(nums, i + 1, res, path + [nums[i]])