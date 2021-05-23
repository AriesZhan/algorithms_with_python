# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param l1 ListNode类 
# @param l2 ListNode类 
# @return ListNode类
#
class Solution:
    def mergeTwoLists(self , l1 , l2 ):
        if not l1:
            return l2
        if not l2:
            return l1
        head = None
        tail = None
        l1_ref = l1
        l1_rest = l1.next
        l2_ref = l2
        l2_rest = l2.next
        if l1_ref.val <= l2_ref.val:
            tail = head = l1_ref
            l1_ref = l1_rest
        else:
            tail = head = l2_ref
            l2_ref = l2_rest
        while (l1_ref and l2_ref):
            if l1_ref.val <= l2_ref.val:
                l1_rest = l1_ref.next
                tail.next = l1_ref
                tail = l1_ref
                l1_ref = l1_rest
            elif l1_ref.val > l2_ref.val:
                l2_rest = l2_ref.next
                tail.next = l2_ref
                tail = l2_ref
                l2_ref = l2_rest
        if l1_ref:
            tail.next = l1_ref
        elif l2_ref:
            tail.next = l2_ref
        return head
            
            # write code here