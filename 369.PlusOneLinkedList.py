# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def helper(node):
            if not node.next:
                node.val, carry = (node.val + 1)%10, (node.val + 1)//10
                return carry
            pre_carry = helper(node.next)
            node.val, carry = (node.val + pre_carry)%10, (node.val + pre_carry)//10
            return carry
        pre_carry = helper(head)
        dummy = ListNode(1)
        dummy.next = head
        if pre_carry:
            head = dummy
        return head