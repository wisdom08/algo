# https://leetcode.com/problems/contains-duplicate/
# 회고: if문 제거 가능
class Solution(object):
    def containsDuplicate(self, nums):
        set_nums = set(nums)
        if len(nums) == len(set_nums):
            return False
        else:
            return True
