# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, value=0, nxt=None):
        self.val = value
        self.next = nxt

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        p1 = l1
        p2 = l2
        # pointer to traverse the resulting list
        curr = res
        carry = 0

        while p1 is not None or p2 is not None or carry != 0:
            temp_sum = carry

            if p1:
                temp_sum += p1.val
                p1 = p1.next

            if p2:
                temp_sum += p2.val
                p2 = p2.next
            curr.val = temp_sum % 10
            carry = temp_sum // 10

            if p1 is not None or p2 is not None or carry != 0:
                curr.next = ListNode()
                curr = curr.next

        return res
