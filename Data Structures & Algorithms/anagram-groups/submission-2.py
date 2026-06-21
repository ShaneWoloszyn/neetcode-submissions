class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sList = ["".join(sorted(s)) for s in strs]
        ansMap = {}
        ans = []

        for i, s in enumerate(sList):
            if s in ansMap:
                ansMap[s].append(i)
            else:
                ansMap[s] = [i]
        
        i = 0
        for key, tok in ansMap.items():
            ans.append([])
            for t in tok:
                ans[i].append(strs[t])
            i += 1
        

        return ans