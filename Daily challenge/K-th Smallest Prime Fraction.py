class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                f = (arr[i] / arr[j], (arr[i], arr[j]))
                heappush(minHeap, f)
        
        for _ in range(k - 1):
            heappop(minHeap)
        
        return heappop(minHeap)[1]