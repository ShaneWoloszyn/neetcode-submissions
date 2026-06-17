class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustIn = [0] * (n + 1)
        trustOut = [0] * (n + 1)

        for t in trust:
            trustIn[t[1]] += 1
            trustOut[t[0]] += 1

        for i in range(n + 1):
            print(i, trustIn[i], trustOut[i])
            if trustIn[i] == n - 1 and trustOut[i] == 0:
                return i
        return -1