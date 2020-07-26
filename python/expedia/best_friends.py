import collections

class Solution:
    def findMiniScoreTrio(self, edges):
        def helper(cur, path):
            if graph.get(cur):
                for t in graph.get(cur):
                    if len(path) == 3:
                        if t == path[0]:
                            trios.add(tuple(sorted(path[-2:] + [t])))
                    else:
                        helper(t, path + [t])

        graph = collections.defaultdict(list)
        for fr, t in edges:
            graph[fr].append(t)
        trios = set()
        for fr in graph.keys():
            helper(fr, [fr])
        return min([len(graph[trio[0]]) + len(graph[trio[1]]) + len(graph[trio[2]]) for trio in trios])

if __name__ == '__main__':
    edges = [[1, 2], [2, 1], [2, 4], [2, 5], [3,2], [3, 5], [4, 2], [4, 5], [5, 2], [5, 3], [5, 4], [5, 6], [6,4], [6,5]]

    solu = Solution()
    print(solu.findMiniScoreTrio(edges))