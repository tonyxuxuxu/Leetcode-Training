"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.get_permute([], nums, result)
        return result

    def get_permute(self, current, nums, result):
        if not nums:
            result.append(current+[])
            return
        for index, value in enumerate(nums):
            current.append(nums[index])
            self.get_permute(current, nums[:index]+nums[index+1:], result)
            current.pop()

if __name__ == '__main__':
    input = [1, 2, 3]
    sol =Solution()
    print(sol.permute(input))
