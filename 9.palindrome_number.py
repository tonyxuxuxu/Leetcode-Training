"""

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution1:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        strx = str(x)
        reversed_strx = strx[::-1]
        if reversed_strx == strx:
            return True
        else:
            return False


class Solution2:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        div = 1
        while x/div >= 10:
            div *= 10
        while x != 0:
            left = x / div
            right = x % 10
            if left != right:
                return False
            x = (x % div) / 10
            div /= 100
        return True

if __name__ == '__main__':
    sol1 = Solution1()
    print(sol1.isPalindrome(1213))

    sol2 = Solution2()
    print(sol1.isPalindrome(1213))
