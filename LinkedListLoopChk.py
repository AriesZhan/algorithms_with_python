# class ListNode:
#     def __init__(self):
#         self.val = None
#         self.next = ListNode()

# {1,2,3,4,5,6,7,8,4}, 4 would be the loop beginning.
# slow pointer move 1 step.
# fast pointer move 2 steps before first encountering and move 1 step after.
# it would be the loop beginning when sp and fp make 2nd encountering.

def LinkedListLoopChk(head):
    sp = head
    fp = head
    met = 0
    loop = False
    while fp.next and fp.next.next:
        if met:
            fp = fp.next
        else:
            fp = fp.next.next
        sp = sp.next
        if sp == fp and not met:
            fp = head
            met = 1
        elif sp == fp and met:
            loop = sp
            break
    return loop
