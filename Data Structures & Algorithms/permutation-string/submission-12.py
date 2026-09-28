class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        want = {}
        have = {}

        for i in range(len(s1)):
            want[s1[i]] = 1 + want.get(s1[i], 0)
            have[s2[i]] = 1 + have.get(s2[i], 0)
        
        if want == have:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            have[s2[l]] -= 1
            if have[s2[l]] == 0:
                del have[s2[l]]
            l += 1
            have[s2[r]] = 1 + have.get(s2[r], 0)
            if want == have:
                return True
        
        return False