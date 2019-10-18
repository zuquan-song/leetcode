# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseNode(begin, end):
            # d->1<-2<-3<-4->5
            # b  f        c  e
            cur = begin.next
            first, prev = cur, begin
            while cur != end:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            first.next = cur
            begin.next = prev
            return first
        
        # d->1->2->3->4->5, 2
        # b        e
        dummy = ListNode(-1)
        dummy.next, i, pre = head, 0, dummy
        post = head
        while post:
            i += 1
            if i % k == 0:
                pre = reverseNode(pre, post.next)
                post = pre.next
            else:
                post = post.next
        return dummy.next 
