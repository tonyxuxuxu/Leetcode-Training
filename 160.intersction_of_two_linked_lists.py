"""

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def get_length(node):
            length = 0
            while node:
                node = node.next
                length += 1
            return length

        a_length = get_length(headA)
        b_length = get_length(headB)
        if a_length > b_length:
            for _ in range(a_length - b_length):
                headA = headA.next
        else:
            for _ in range(b_length - a_length):
                headB = headB.next
        while headA:
            if headA == headB:
                return headA
            headB = headB.next
            headA = headA.next
        return None