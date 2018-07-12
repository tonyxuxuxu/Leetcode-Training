"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        temp = dummy
        while temp:
            temp = self.reverseNextK(temp, k)
        return dummy.next

    def reverseNextK(self, head, k):
        # Check if there are k nodes left
        temp = head
        for i in range(k):
            if not temp.next:
                return None
            temp = temp.next

        # The last node when the k nodes reversed
        node = head.next
        prev = head
        curr = head.next
        # Reverse k nodes
        for i in range(k):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        # Connect with head and tail
        node.next = curr
        head.next = prev
        return node