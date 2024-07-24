class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        hash_table = {}
        mapped = {}
        index = {}
        for i in range(len(mapping)):
            hash_table[i] = mapping[i]

        for i, n in enumerate(nums):
            index[n] = i
            value = ""
            n = str(n)
            for digit in n:
                value += str(hash_table[int(digit)])
            mapped[int(n)] = int(value)

        nums.sort(key=lambda n: (mapped[n], index[n]))
        return nums
