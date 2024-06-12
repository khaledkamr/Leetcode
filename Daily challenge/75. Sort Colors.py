class Solution:
    def sortColors(self, nums: List[int]) -> None:
        hash_map = Counter(nums)
        nums.clear()
        nums.extend([0] * hash_map[0])
        nums.extend([1] * hash_map[1])
        nums.extend([2] * hash_map[2])
