class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = dict()
        for i in nums:
            s[i] = s.get(i, 0) + 1

        res = []
        for i in range(len(s)):
            if s[i] == 2:
                res.append(i)

        return res

            