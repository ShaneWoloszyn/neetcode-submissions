class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()

        def search(r, c, visit, lastHeight):
            if r < 0 or r > len(heights) - 1 or c < 0 or c > len(heights[0]) - 1 or heights[r][c] < lastHeight or (r, c) in visit:
                return
            
            visit.add((r, c))
            search(r - 1, c, visit, heights[r][c])
            search(r + 1, c, visit, heights[r][c])
            search(r, c - 1, visit, heights[r][c])
            search(r, c + 1, visit, heights[r][c])
        
        for r in range(len(heights)):
            search(r, 0, pac, heights[r][0])
            search(r, len(heights[0]) - 1, atl, heights[r][len(heights[0]) - 1])
        
        for c in range(len(heights[0])):
            search(0, c, pac, heights[0][c])
            search(len(heights) - 1, c, atl, heights[len(heights) - 1][c])
        
        res = []

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res