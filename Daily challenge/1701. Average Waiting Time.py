class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        Sum = 0
        prep = customers[0][0]
        for order in customers:
            prep = max(prep, order[0])
            prep += order[1]
            Sum += prep - order[0]

        return Sum / len(customers)
