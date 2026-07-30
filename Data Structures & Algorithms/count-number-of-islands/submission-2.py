class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Row = len(grid)
        Col = len(grid[0])
        visited = set()
        island = 0

        def dfs(r, c):
            if (r < 0 or
                c < 0 or
                r >= Row or
                c >= Col or 
                grid[r][c] != "1" or
                (r,c) in visited ):
                return False
            visited.add((r,c))
            dfs(r+1 ,c) or dfs(r, c+1) or dfs(r-1, c) or dfs(r, c-1)

        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    island += 1
                    dfs(r, c)
        return island