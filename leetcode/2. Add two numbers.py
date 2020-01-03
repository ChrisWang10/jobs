"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(0)
        cur = ret
        carry = 0
        while l1 and l2:
            carry, next_value = divmod(l1.val + l2.val + carry, 10)
            cur.next = ListNode(next_value)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        while l1:
            carry, next_value = divmod(l1.val + carry, 10)
            cur.next = ListNode(next_value)
            l1 = l1.next
            cur = cur.next
        while l2:
            carry, next_value = divmod(l2.val + carry, 10)
            cur.next = ListNode(next_value)
            l2 = l2.next
            cur = cur.next
        while carry:
            cur.next = ListNode(carry)
            carry = 0

        return ret.next
