import collections
class Node:
    def __init__(self, v=0, idx=0):
        self.val = v
        self.counter = 1
        self.index = idx
        self.prev = None
        self.next = None

def find_unique_character(s):
    if not len(s): return -1

    dummy, tail = Node(), Node()
    dummy.next, tail.prev = tail, dummy
    pointers = {}
    res = []
    for i, ch in enumerate(s):
        if ch not in pointers:
            node = Node(ch, i)
            first = dummy.next
            node.next, node.prev = first, dummy
            dummy.next, first.prev = node, node
            pointers[node.val] = node
        else:
            pointers[ch].counter += 1

        while tail.prev != dummy and tail.prev.counter > 1:
            tail.prev = tail.prev.prev
        tail.prev.next = tail
        if tail.prev == dummy:
            res.append((-1, -1))
        else:
            res.append((tail.prev.val, tail.prev.index))
    return res

print(find_unique_character("loveleetcodevffftcddd"))