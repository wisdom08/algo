# https://leetcode.com/problems/top-k-frequent-elements/
# 회고: 나중에 heap을 써서 개선할 수 있을 것 같다.
class Solution(object):
    def topKFrequent(self, nums, k):
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        sorted_frequency = sorted(frequency, key=lambda num: frequency[num])
        return sorted_frequency[-k:]
