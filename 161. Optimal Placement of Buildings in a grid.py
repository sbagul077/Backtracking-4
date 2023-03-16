from collections import deque


class BuildingPlacement:
    minDistance = 0

    def findMinDistance(self, H, W, n):
        grid = [[-1 for i in range(W)] for j in range(H)]
        self.minDistance = float("inf")
        self.backtrack(grid, 0, 0, n, H, W)
        return self.minDistance

    def bfs(self, grid, H, W):
        q = deque()
        # grid with particular placement of buildings
        visited = [[False] * W for i in range(H)]

        for i in range(H):
            for j in range(W):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited[i][j] = True

        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        dist = 0
        while q:
            size = len(q)
            for k in range(size):
                curr = q.popleft()
                for d in dirs:
                    nr = curr[0] + d[0]
                    nc = curr[1] + d[1]

                    if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == -1 and not visited[nr][nc]:
                        q.append([nr, nc])
                        visited[nr][nc] = True
            dist += 1
            # print(dist)
        # we compare with dist - 1. as for the last level also we are increasing the distance by 1
        self.minDistance = min(self.minDistance, dist - 1)

    def backtrack(self, grid, r, c, n, H, W):
        # base
        if n == 0:
            self.bfs(grid, H, W)
            return
        # logic
        # if we are going out of bounds, we reset the column to 0
        if c == W:
            r += 1
            c = 0

        for i in range(r, H):
            for j in range(c, W):
                # action
                # print(grid[i][j], i , j, len(grid), len(grid[0]), grid)
                grid[i][j] = 0
                # recurse
                self.backtrack(grid, i, j + 1, n - 1, H, W)
                # backtrack
                grid[i][j] = -1


class Solution:
    def __int__(self):
        self.buildingPlacement = BuildingPlacement()
        print(self.buildingPlacement.findMinDistance(4, 4, 2), [4, 4, 2])
        print(self.buildingPlacement.findMinDistance(3, 2, 1), [3, 2, 1])


if __name__ == "__main__":
    obj = Solution()
    obj.__int__()

# Backtrack Recursion
# Time Complexity : O(((h*w) C n) *(h*w)), Where h, w are height,width of the 2d array respectively
#SpaceComplexity: O(HW)

