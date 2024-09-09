class Solution:
    def compress(self, chars: list[str]) -> int:
        res = ""
        group = []
        for i in range(len(chars)):
            if len(group) == 0:
                group.append(chars[i])
            elif chars[i] == group[0]:
                group.append(chars[i])
            else:
                res += group[0] + str(len(group)) if len(group) > 1 else group[0]
                group.clear()
                group.append(chars[i])

        if len(group) > 0:
            res += group[0] + str(len(group)) if len(group) > 1 else group[0]

        for i in range(len(res)):
            chars[i] = res[i]
        return len(res)
