class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        sum, i = 0, 0
        while k:
            sum += happiness[i] - i if happiness[i] - i > 0 else 0 
            i += 1
            k -= 1
        return sum