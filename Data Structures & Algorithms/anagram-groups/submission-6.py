class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            if tuple(count) in res:
                res[tuple(count)].append(s)
            else:
                res[tuple(count)] = [s]
        
        return list(res.values())