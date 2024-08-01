class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for element in details:
            if int(element[11:13]) > 60:
                res += 1

        return res
