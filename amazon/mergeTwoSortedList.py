# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        cursor = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cursor.next = l1
                cursor, l1 = cursor.next, l1.next
            else:
                cursor.next = l2
                cursor, l2 = cursor.next, l2.next
        if not l1:
            cursor.next = l2
        else:
            cursor.next = l1
        return dummy.next