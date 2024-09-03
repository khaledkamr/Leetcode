class Solution:
    def getLucky(self, s: str, k: int) -> int:
        converted = ""
        for c in s:
            converted += str(ord(c) - ord("a") + 1)

        while k:
            converted = [int(i) for i in converted]
            Sum = sum(converted)
            converted = str(Sum)
            k -= 1

        return int(converted)
