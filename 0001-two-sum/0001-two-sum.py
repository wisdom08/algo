# https://leetcode.com/problems/two-sum/
# 회고: 해시테이블을 이용해서 시간복잡도를 개선할 수 있음
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]