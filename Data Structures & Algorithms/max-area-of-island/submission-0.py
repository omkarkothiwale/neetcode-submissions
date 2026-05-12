class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_area = 0
        temp_sum = 0
        def dfs(r, c):
            nonlocal temp_sum
            if (r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0):
                return
            grid[r][c] = 0
            temp_sum += 1
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    max_area = max(max_area, temp_sum)
                    temp_sum = 0
        return max_area