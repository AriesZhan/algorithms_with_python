class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
#
# @param head ListNode类
# @param n int整型
# @return ListNode类
#


class Solution:
    def removeNthFromEnd(head, n):
        p1 = None
        p2 = head
        i = 0
        while p2:
            p2 = p2.next
            i += 1
            if i == n+1:
                p1 = head
            elif p1:
                p1 = p1.next
        if not p1:
            return head.next
        else:
            p1.next = p1.next.next
            return head
