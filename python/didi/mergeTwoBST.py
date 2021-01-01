
class Node:

    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    @classmethod
    def viz(cls, node, res):
        if not node: return
        Node.viz(node.left, res)
        res.append(node.val)
        Node.viz(node.right, res)

def merge(left, right):
    def helper(node, cur):
        if not node:
            return

        if node.val > cur.val:
            if not node.left:
                node.left = cur
                cur.left, cur.right = None, None
            else:
                helper(node.left, cur)
        else:
            if not node.right:
                node.right = cur
                cur.left, cur.right = None, None
            else:
                helper(node.right, cur)

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        helper(left, node)

    dfs(right)
    return left



if __name__ == '__main__':
    #    5
    #  2   8
    # 1 4 6 10

    #   11
    #  3  16
    a, b, c, d, e, f, g = Node(5), Node(2), Node(8), Node(1), Node(4), Node(6), Node(10)
    h, i, j = Node(11), Node(3), Node(16)
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    h.left, h.right = i, j
    merge(a, h)
    res = []
    Node.viz(a, res)
    print(res)
