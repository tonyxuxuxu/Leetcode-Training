"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        mid = 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = int((left + right)/2)
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[mid]
