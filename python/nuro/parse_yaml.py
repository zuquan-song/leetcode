class TreeNode:

    def __init__(self, key, childs):
        self.key = key
        self.childs = childs # {}

    def getVal(self, input):
        def helper(path, node):
            if len(path) == 0:
                return node

            if path[0] in node.childs:
                return helper(path[1:], node.childs[path[0]])
            else:
                return None

        path = input.split('.')
        return helper(path, self).key

def parse_yaml(input):
    def getIndent(line):
        count = 0
        while line[count] == ' ':
            count += 1
        return count
    lines = input.split("\n")
    n = len(lines)
    cursor = 0
    def dfs(node, prevIndent):
        nonlocal cursor

        while cursor < n:
            line, cursor = lines[cursor], cursor + 1
            if line.strip() == "":
                continue
            key, val = line.strip().split(":")
            cur_indent = getIndent(line)

            if cur_indent > prevIndent:
                if val != "":
                    new = TreeNode(key, val)
                    node.childs[key] = new
                else:
                    new = TreeNode(key, {})
                    node.childs[key] = new
                    dfs(new, cur_indent)
            else:
                cursor -= 1
                return

    root = TreeNode('root', {})
    dfs(root, -1)
    return root

input = '''
k1:v1
k2:
  k21:v2
  k22:
             k211:v211
  k23:
      k231:v231
k3:v3
'''

root = parse_yaml(input)
print(root.getVal("k2.k22.k211"))