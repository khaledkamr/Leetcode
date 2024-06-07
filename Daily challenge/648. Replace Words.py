class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        res = []
        for word in sentence.split():
            for dic in dictionary:
                if dic == word[: len(dic)]:
                    word = dic

            res.append(word)

        return " ".join(res)
