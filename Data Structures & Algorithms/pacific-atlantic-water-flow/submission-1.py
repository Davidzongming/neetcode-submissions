class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Row = len(heights)
        Col = len(heights[0])
        pacific = set()
        atlantic = set()
        canFlow = []
        def dfs(r, c, visited, preheights):
            if (r, c) in visited or r < 0 or c < 0 or r >= Row or c>= Col or heights[r][c] < preheights:
                return
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        for r in range(Row):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, Col-1, atlantic, heights[r][Col - 1])

        for c in range(Col):
            dfs(0 , c, pacific, heights[0][c])
            dfs(Row-1, c, atlantic, heights[Row-1][c])

        for r in range(Row):
            for c in range(Col):
                if (r,c) in pacific and (r,c) in atlantic:
                    canFlow.append((r,c))
        return canFlow
                    

