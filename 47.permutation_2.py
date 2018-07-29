"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        self.get_permute([], nums, result)
        return result

    def get_permute(self, current, num, result):
        if not num:
            result.append(current + [])
            return
        for i, v in enumerate(num):
            if i - 1 >= 0 and num[i] == num[i - 1]:
                continue
            current.append(num[i])
            self.get_permute(current, num[:i] + num[i + 1:], result)
            current.pop()