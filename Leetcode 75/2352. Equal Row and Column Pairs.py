class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        count = 0
        freq = defaultdict(int)
        for li in grid:
            freq[tuple(li)] += 1

        col = []
        for i in range(len(grid)):
            col.clear()
            for j in range(len(grid[0])):
                col.append(grid[j][i])

            if freq[tuple(col)] > 0:
                count += freq[tuple(col)]

        return count
