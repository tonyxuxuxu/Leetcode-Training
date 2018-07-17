"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

# stack method
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        matched = [0 for i in range(len(s))]
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            elif char == ')' and len(stack) != 0:
                matched[index] = matched[stack[-1]] = 1
                stack.pop()
        return sum(matched)


if __name__ == '__main__':
    sol = Solution()
    input = ")()())"
    print(sol.longestValidParentheses(input))
