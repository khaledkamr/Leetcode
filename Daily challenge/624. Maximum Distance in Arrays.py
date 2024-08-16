class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        distance = 0
        Min = arrays[0][0]
        Max = arrays[0][-1]
        for i in range(1, len(arrays)):
            distance = max(distance, arrays[i][-1] - Min, Max - arrays[i][0])
            Min = min(Min, arrays[i][0])
            Max = max(Max, arrays[i][-1])

        return distance
