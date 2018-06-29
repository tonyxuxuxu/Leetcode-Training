"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums1_len = len(nums1)
        nums2_len = len(nums2)

        all_nums = []
        p1 = p2 = 0
        while p1 < nums1_len and p2 < nums2_len:
            if nums1[p1] < nums2[p2]:
                all_nums.append(nums1[p1])
                p1 += 1
            else:
                all_nums.append(nums2[p2])
                p2 += 1
        if p1 < nums1_len:
            while p1 < nums1_len:
                all_nums.append(nums1[p1])
                p1 += 1
        if p2 < nums2_len:
            while p2 < nums2_len:
                all_nums.append(nums2[p2])
                p2 += 1

        if (nums1_len + nums2_len) % 2 == 1:
            median = all_nums[int((nums1_len+nums2_len)/2)]
        else:
            median = (all_nums[int((nums1_len+nums2_len)/2)] + all_nums[int((nums1_len+nums2_len)/2-1)])/2
        return median


if __name__ == '__main__':
    sol1 = Solution()
    num1 = [1, 2]
    num2 = [3, 4]
    print(sol1.findMedianSortedArrays(num1, num2))