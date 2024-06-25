class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lastIndex = 0
        for i, e in enumerate(s):
            cur = t.find(e, lastIndex, len(t))
            if lastIndex == -1:
                return False
            elif cur < lastIndex:
                return False
            else:
                t = t.replace(e, '@', 1)
                lastIndex = cur

        return True

        