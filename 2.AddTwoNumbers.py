# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp1, tmp2 = l1, l2
        rlt = ListNode((l1.val + l2.val) % 10)
        cursor = rlt
        add = int((tmp1.val + tmp2.val) / 10)

        while tmp1 or tmp2:
            tmp1, tmp2 = tmp1.next if tmp1 else None, tmp2.next if tmp2 else None
            if not tmp1 and not tmp2:
                break
            mode = ((tmp1.val if tmp1 else 0) + (tmp2.val if tmp2 else 0) + add) % 10
            add = int(((tmp1.val if tmp1 else 0) + (tmp2.val if tmp2 else 0) + add) / 10)
            cur_node = ListNode(mode)
            cursor.next, cursor = cur_node, cur_node

        if add == 1:
            cur_node = ListNode(1)
            cursor.next = cur_node
        return rlt
