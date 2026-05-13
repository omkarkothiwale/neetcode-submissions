class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)

        if grid[0][0] == 1 or grid[N-1][N-1]:
            return -1
        q = deque([(0, 0, 1)])
        visited = set((0, 0))
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while q:
            r, c, length = q.popleft()

            if r == N-1 and c == N-1:
                return length

            for dr, dc in directions:
                nr = r+dr
                nc = c+dc
                if (nr in range(N) and nc in range(N) and grid[nr][nc] == 0 and (nr, nc) not in visited):
                    q.append((nr, nc, 1+length))
                    visited.add((nr, nc))
        return -1