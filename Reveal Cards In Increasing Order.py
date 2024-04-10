class Solution(object):
    def deckRevealedIncreasing(self, deck):
        res = deque()
        deck.sort()
        deck.reverse()

        for card in deck:
            if res:
                temp = res.popleft()
                res.append(temp)
            res.append(card)

        res = list(res)
        res.reverse()
        return res