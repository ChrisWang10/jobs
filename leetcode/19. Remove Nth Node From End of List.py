"""
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getListLength(self, head):
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return length

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return head
        listLength = self.getListLength(head)
        print(listLength)
        if n > listLength:
            return head
        elif n == listLength:
            return head.next
        else:
            cur = head
            mark = listLength - n
            cnt = 0
            while cur:
                print(cur.val)
                pre = cur
                cur = cur.next
                cnt += 1
                if cnt == mark:
                    pre.next = cur.next
        return head


root = ListNode(1)

so = Solution()
so.removeNthFromEnd(root, 1)
