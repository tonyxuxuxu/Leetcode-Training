"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            num1 = nums[i]
            if target - num1 in dict:
                return dict[target - num1], i
            dict[num1] = i


class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens = len(nums)
        for i in range(lens):
            for j in range(i+1, lens):
                if nums[i] + nums[j] == target:
                    return i,j


class Solution3:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()
        begin, end = 0, len(nums_index) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1

class Solution4:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_nums = {}
        for index, num in enumerate(nums):
            another = target - num
            try:
                hash_nums[another]
                return [hash_nums[another], index]
            except:
                hash_nums[num] = index

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solu4 = Solution4()
    print(solu4.twoSum(nums, target))
