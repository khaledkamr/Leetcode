class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        hash_map = Counter(arr1)
        for n in arr2:
            for i in range(hash_map[n]):
                res.append(n)
                arr1.remove(n)
        arr1 = sorted(arr1)
        res.extend(arr1)
        return res
