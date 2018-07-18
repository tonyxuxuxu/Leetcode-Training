"""

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = int((low+high)/2)
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                result.append(mid)
                break
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        if not result:
            return [-1, -1]

        high = len(nums) - 1
        while low <= high:
            mid = int((low+high)/2)
            if nums[mid] == target and (mid == 0 or nums[mid+1] != target):
                result.append(mid)
                break
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return result


if __name__ == '__main__':
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(sol.searchRange(nums, target))