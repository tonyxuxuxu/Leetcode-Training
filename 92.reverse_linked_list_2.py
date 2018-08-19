"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy

        for _ in range(m-1):
            node = node.next
        prev = node.next
        curr = prev.next
        for _ in range(n - m):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        node.next.next = curr
        node.next = prev
        return dummy.next