
class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BSTIterator():

    def __init__(self, root):
        self.stack = []
        cur = root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    def next(self):
        node = self.stack.pop()
        cur = node.right
        while cur:
            self.stack.append(cur)
            cur = node.left

        return node.val
