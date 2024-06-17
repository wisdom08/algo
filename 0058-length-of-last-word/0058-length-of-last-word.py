class Solution:
    def lengthOfLastWord(self, s: str) -> int:
            r = s.split(' ')

            for i in range(len(r) - 1, -1, -1):
                if r[i] != '':
                    return len(r[i])
        