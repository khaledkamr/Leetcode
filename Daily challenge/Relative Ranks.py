class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = {}
        res = list(score)
        score.sort()
        score.reverse()
        for i in range(len(score)):
            if i == 0:
                dic[score[i]] = "Gold Medal"
            elif i == 1:
                dic[score[i]] = "Silver Medal"
            elif i == 2:
                dic[score[i]] = "Bronze Medal"
            else:
                dic[score[i]] = str(i + 1)
        
        for i in range(len(score)):
            res[i] = dic[res[i]]
        
        return res