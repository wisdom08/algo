# https://leetcode.com/problems/remove-element/
# 회고: 리스트 길이만큼 맨 앞의 요소를 검사해서 val이면 제거하고, 아니면 뒤로 보냄
class Solution:
    def removeElement(self, nums, val):
        for i in range(len(nums)):
            if nums[0] != val:
                nums.append(nums[0])
                del nums[0]
            else:
                del nums[0]
        return len(nums)