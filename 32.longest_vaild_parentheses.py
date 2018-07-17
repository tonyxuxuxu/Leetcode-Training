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
class Solution1:
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


# Dynamic Progamming
class Solution2:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        return max(dp)


if __name__ == '__main__':
    sol = Solution2()
    input = ")()())"
    print(sol.longestValidParentheses(input))
