import collections

def graph_circle(A, B):
    # start -> ... -> visited_node
    # visted_node == start
    # visted_node is the same as N verticals
    n = len(A)
    if n != len(B):
        return False
    visited = [False] * (n+1)

    graph = collections.defaultdict(list)
    for st, ed in zip(A, B):
        graph[st].append(ed)
        if len(graph[st]) > 1:
            return False

    start, cur = A[0], A[0]
    while not visited[cur]:
        visited[cur] = True
        if len(graph[cur]) == 0:
            return False
        cur = graph[cur][0]

    if cur == start and all(v == True for v in visited[1:]):
        return True
    return False

if __name__ == '__main__':
    print(graph_circle([1,3,2,4], [4,1,3,2]))
    print(graph_circle([1,2,3,4], [2,1,4,3]))