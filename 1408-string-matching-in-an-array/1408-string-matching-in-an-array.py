# https://leetcode.com/problems/string-matching-in-an-array
# 회고: 데이터가 크지 않아 Brute Force이 효율적인 문제
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        answer = []

        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    answer.append(words[i])
                    break
        
        return answer