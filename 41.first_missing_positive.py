"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        i = 0
        length = len(nums)
        while i < length:
            current = nums[i]
            if current <= 0 or current > length or nums[current - 1] == current:
                i += 1
            else:
                nums[current - 1], nums[i] = nums[i], nums[current - 1]
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1

if __name__ == '__main__':
    sol = Solution()
    Input = [15,6,7,3,4,-1,1]
    print(sol.firstMissingPositive(Input))