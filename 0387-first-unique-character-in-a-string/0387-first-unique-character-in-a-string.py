class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}

        for i in s:
            if i not in unique:
                unique[i] = 1
            else:
                unique[i] = unique[i] + 1

        for i in range(0, len(s)):
            if unique[s[i]] == 1:
                return i
        
        return -1
        