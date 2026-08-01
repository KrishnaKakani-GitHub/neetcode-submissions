from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # sorted string -> list of anagrams

        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)

        return list(res.values())
