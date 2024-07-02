class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        res = []

        for n in nums2:
            if count1[n]:
                res.append(n)
                count1[n] -= 1

        return res
