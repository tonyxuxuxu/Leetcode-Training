"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, curMax, curMin = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            curMax, curMin = max(num, num*curMax, num*curMin), min(num, num*curMax, num*curMin)
            result = max(curMax, result)
        return result

if __name__ == '__main__':
    sol = Solution()
    input = [2, 3, -2, 4]
    print(sol.maxProduct(input))