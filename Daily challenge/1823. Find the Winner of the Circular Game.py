class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = []
        for i in range(n):
            circle.append(i + 1)

        i = 0
        while len(circle) > 1:
            i = (i + k - 1) % len(circle)
            circle.pop(i)

        return circle[0]
