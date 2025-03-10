class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        res = []
        for i in range(len(s)):
            if i == k:
                break
            else:
                res.append(s[i])

        return ' '.join(res)