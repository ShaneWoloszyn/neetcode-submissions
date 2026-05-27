class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sMap = defaultdict(list)

        for s in strs:
            sSorted = ''.join(sorted(s))
            sMap[sSorted].append(s)
        return list(sMap.values())