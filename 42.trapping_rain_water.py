"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # left_height, right_height = [], []
        # left, right, water = 0, 0, 0
        # for i in height:
        #     left = max(left, i)
        #     left_height.append(left)
        # print(left_height)
        # for j in reversed(height):
        #     right = max(right, j)
        #     right_height.append(right)
        # print(right_height)
        # for index, height in enumerate(height):
        #     left = left_height[index]
        #     right = right_height[index]
        #     water += min(left, right) - height
        # return water
        result, left, right, water = [], 0, 0, 0
        for i in height:
            left = max(left, i)
            height.append(left)
        height.reverse()
        for n, i in enumerate(reversed(height)):
            right = max(right, i)
            water += min(result[n], right) - i
        return water


if __name__ == '__main__':
    sol = Solution()
    input = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(sol.trap(input))