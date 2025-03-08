# 회고: 시간 복잡도 O(N), 공간 복잡도 O(1) 간단한 문제
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if i % 3 != 0:
                res += 1
        
        return res