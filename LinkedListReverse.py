# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        while pHead:
            p1 = pHead
            if pHead.next:
                p2 = pHead.next
                pHead = pHead.next
                p1.next = None
            else:
                return pHead
            while pHead.next:
                pHead = pHead.next
                p2.next = p1
                p1 = p2
                p2 = pHead
            pHead.next = p1
            return pHead
    