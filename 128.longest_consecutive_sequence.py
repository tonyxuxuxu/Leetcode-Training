"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 0
        if not nums:
            return 0
        numsset = set(nums)
        for n in nums:
            currlen, temp = 1, n + 1
            while temp in numsset:
                currlen += 1
                numsset.discard(temp)
                temp += 1
            temp = n -1
            while temp in numsset:
                currlen += 1
                numsset.discard(temp)
                temp -= 1
            maxlen = max(currlen, maxlen)
        return maxlen