class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        direction = [[0,-1], [0, 1], [1, 0], [-1, 0]]
        ROWS, COLUMNS = len(grid), len(grid[0])
        isIsland = 0

        def dfs(r, c):

            if (r < 0 or c < 0 or r > ROWS -1 or c > COLUMNS - 1 or grid[r][c] == "0"):
                return

            grid[r][c] = "0"

            for row, col in direction:
                dfs(r + row, c + col)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if (grid[r][c] == "1"):
                    dfs(r, c)
                    isIsland += 1

        return isIsland