"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i = 0
        result = 0
        distance = pow(2, 32) - 1
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                l = [nums[i], nums[j], nums[k]]
                if sum(l) == target:
                    return target
                if abs(sum(l) - target) < distance:
                    result = sum(l)
                    distance = abs(sum(l) - target)
                elif sum(l) > target:
                    k -= 1
                else:
                    j += 1
        return result

if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    print(sol.threeSumClosest(nums, target))
