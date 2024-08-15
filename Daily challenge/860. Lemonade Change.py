class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        cash = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                cash[bill] += 1
            elif bill == 10:
                if cash[5]:
                    cash[10] += 1
                    cash[5] -= 1
                else:
                    return False
            else:
                if cash[10] and cash[5]:
                    cash[20] += 1
                    cash[10] -= 1
                    cash[5] -= 1
                elif cash[5] > 2:
                    cash[20] += 1
                    cash[5] -= 3
                else:
                    return False

        return True
