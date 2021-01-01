
def getPoorGuy(bidders, share):
    bidders.sort(key=lambda x: (x[2], -x[3]))

    while share > 0:
        bidder = bidders[-1]
        price = bidder[2]
        i = len(bidders) - 1
        while i > 0 and bidders[i-1][2] == price:
            i -= 1

        if i == len(bidders) - 1:
            share -= min(share, bidder[1])
            bidders.pop()
        else:
            leftmost = len(bidders) - 1
            while share > 0 and any([req != 0 for req in bidders[i: len(bidders)]]):
                l, r = i, len(bidders) - 1
                while share > 0 and any([req != 0 for req in bidders[i: len(bidders)]]):
                    if bidders[r][1] > 0 and share > 0:
                        bidders[r][1] -= 1
                        share -= 1
                    print(bidders, share)
                    r -= 1
                    leftmost = min(leftmost, r)
                    if l > r:
                        r = len(bidders) - 1

            if share == 0:
                return [bd[0] for bd in bidders[:leftmost+1]]

            rmBidder = i
            while len(bidders) > rmBidder:
                bidders.pop()
        print(bidders, share)
    return [bd[0] for bd in bidders]

print(getPoorGuy([[1,5,5,1],
                  [2,7,7,3],
                  [3,7,5,2],
                  [4,10,3,0]], 18))