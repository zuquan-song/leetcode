import collections
from typing import List

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    for s in strs:
        ss = "".join(sorted(s))
        anagrams[ss].append(s)
    return [gs for gs in anagrams.values()]