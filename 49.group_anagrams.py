"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        for index, value in enumerate(strs):
            target = "".join(sorted(value))
            if target not in map:
                map[target] = [value]
            else:
                map[target].append(value)

        result = []
        for value in map.values():
            result += [sorted(value)]
        return result

if __name__ == '__main__':
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print(sol.groupAnagrams(input))
