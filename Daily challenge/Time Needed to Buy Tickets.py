class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        count = 0
        while True:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    count += 1

                if tickets[k] == 0:
                    return count
        