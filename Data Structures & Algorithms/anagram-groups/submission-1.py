class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        iList = []
        sMap = {}
        t = 0
        for i, s in enumerate(strs):
            temp = str(sorted(s))
            if temp in sMap:
                iList[sMap[temp]].append(i)
            else:
                sMap[temp] = t
                iList.append([i])
                t += 1
        ans = []

        for i in range(len(iList)):
            arr = []
            for j in iList[i]:
                arr.append(strs[j])
            ans.append(arr)
        return ans