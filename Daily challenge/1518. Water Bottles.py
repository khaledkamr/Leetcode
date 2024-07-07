class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        drink = 0

        while full > 0:
            drink += full
            empty += full
            full = empty // numExchange
            empty %= numExchange

        return drink
