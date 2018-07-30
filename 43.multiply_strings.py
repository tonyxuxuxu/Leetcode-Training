"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution1(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1)*int(num2))

class Solution2(object):
    # https://leetcode.com/problems/multiply-strings/discuss/17605/easiest-java-solution-with-graph-explanation
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0]*(len(num1)+len(num2))
        for i, x in enumerate(reversed(num1)):
            for j, y in enumerate(reversed(num2)):
                a = int(x) * int(j) + result[i+j]
                result[i+j] = int(a%10)
                result[i+j+1] += int(a/10)
        last = 0
        for i in range(len(result)-1, -1, -1):
            if result[i] != 0:
                last = i
                break
            answer = "".join(map(str, reversed(result[0:last + 1])))
            return answer



