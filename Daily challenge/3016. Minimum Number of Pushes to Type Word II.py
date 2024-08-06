class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = [0] * 26
        for c in word:
            counts[ord(c) - ord("a")] -= 1

        heapq.heapify(counts)
        res = 0
        i = 0
        while counts:
            cnt = -heapq.heappop(counts)
            res += cnt * (1 + i // 8)
            i += 1
        return res
