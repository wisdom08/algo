class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l = len(nums)
        if nums[0] > nums[l - 1]:
            for i in range(l - 1):
                if nums[i] < nums[i + 1]:
                    return False
            return True
        else:
            for i in range(l - 1):
                print(i, nums[i], nums[i + 1])
                if nums[i] > nums[i + 1]:
                    return False
            return True