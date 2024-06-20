class Solution:
    def arraySign(self, nums: List[int]) -> int:
        countNegative = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                countNegative += 1
        
        if countNegative % 2 == 0:
            return 1
        else:
            return -1