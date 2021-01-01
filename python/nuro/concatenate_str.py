LEAF_LEN = 2

class Rope:

    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.string = None
        self.lCount = None


def createRopeStructure(parent, input, l, r):
    node = Rope()
    node.parent = parent

    if (r - l) > LEAF_LEN:
        node.string = None
        node.lCount = (r - l) // 2
        m = (l + r) // 2
        node.left = createRopeStructure(node, input, l, m)
        node.right = createRopeStructure(node, input, m+1, r)
    else:
        node.lCount = r - l
        node.string = input[l: r+1]
    return node


def printstring(node):
    if node is None:
        return ""

    if not node.left and not node.right:
        return node.string
    return printstring(node.left) + printstring(node.right)


def concatenate(node1, node2, n):
    root = Rope()
    root.parent = None
    root.left = node1
    root.right = node2
    node1.parent = node2.parent = root
    root.lCount = n
    return root

if __name__ == '__main__':
    input1 = "Hi This is geeksforgeeks. "
    root1 = createRopeStructure(None, input1, 0, len(input1) - 1)

    input2 = "You are welcome here."
    root2 = createRopeStructure(None, input2, 0, len(input2) - 1)

    root3 = concatenate(root1, root2, len(input1))
    viz = printstring(root3)
    print(viz)

