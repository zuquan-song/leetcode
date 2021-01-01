
from typing import List

def nearest_cities(cities, xs, ys, queries: List):
    locations = dict(zip(cities, [(x, y) for x, y in zip(xs, ys)]))
    res = []
    for q in queries:
        tx, ty = locations[q]
        min_dist, cand = float('inf'), ""
        for citi, loc in locations.items():
            if citi != q and (loc[0] == tx or loc[1] == ty):
                distance = abs(loc[0] - tx) + abs(loc[1] - ty)
                if min_dist > distance:
                    min_dist, cand = distance, citi
                elif min_dist == distance and citi < cand:
                    min_dist, cand = distance, citi

        res.append(cand if cand != "" else "NONE")
    return res

print(nearest_cities(["c1", "c2", "c3"], [3, 2, 1], [3, 2, 3], ["c1", "c2", "c3"]))