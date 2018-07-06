"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution1:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                l = [nums[i], nums[j], nums[k]]
                if sum(l) == 0:
                    result.append(l)
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    while j < k and nums[k+1] == nums[k]:
                        k -= 1
                elif sum(l) < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i-1] == nums[i]:
                i += 1
        return result

class Solution2:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return res

if __name__ == '__main__':
    sol = Solution2()
    input = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(input))
