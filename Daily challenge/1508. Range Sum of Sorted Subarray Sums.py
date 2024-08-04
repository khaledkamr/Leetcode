class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        start, end = 0, 1
        Sum = []
        while start < len(nums):
            Sum.append(sum(nums[start:end]))
            end += 1
            if end > len(nums):
                start += 1
                end = start + 1

        Sum.sort()
        return sum(Sum[left - 1 : right]) % (10**9 + 7)
