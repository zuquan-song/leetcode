import collections
import heapq

def streaming(data, k):

    top1, top2 = float('inf'), float('inf')
    counter = collections.defaultdict(int)
    res = []
    for i, val in enumerate(data):
        new, removed = val, float('inf')
        counter[new] += 1
        if i >= k:
            removed = data[i-k]
            counter[removed] -= 1
        vals = list({new, removed, top1, top2})
        vals.sort(key=lambda x: (counter[x], -x), reverse=True)
        print(vals)
        res.append(vals[0])
    return res



if __name__ == '__main__':
    print(streaming([1,2,3,4,3,2,1,1,1,1], 3))