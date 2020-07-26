import sys

class Solution:

    def process(self, fromm, too):

        diff = [t - f for f, t in zip(fromm, too)]
        print("from -> to", diff)

if __name__ == '__main__':
    fromm = sys.argv[1]
    too = sys.argv[2]
    frommId = [ord(ch) - ord('a') for ch in fromm.lower()]
    tooId = [ord(ch) - ord('a') for ch in too.lower()]
    print("origin: fromm %s id %s too %s id %s"%(fromm, frommId, too, tooId))
    solu = Solution()
    solu.process(frommId, tooId)