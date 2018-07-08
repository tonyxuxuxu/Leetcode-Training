"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        result = set()
        sumIndex = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] not in sumIndex:
                    sumIndex[nums[i] + nums[j]] = [(i, j)]
                else:
                    sumIndex[nums[i] + nums[j]].append((i, j))

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                sumNeed = target - (nums[i] + nums[j])
                if sumNeed in sumIndex:
                    for index in sumIndex[sumNeed]:
                        if index[0] > j:
                            result.add(tuple(sorted([nums[i], nums[j], nums[index[0]], nums[index[1]]])))
        result = [list(l) for l in result]
        return result

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    sol = Solution()
    print(sol.fourSum(nums, target))