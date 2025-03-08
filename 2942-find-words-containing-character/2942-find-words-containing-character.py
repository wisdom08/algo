# 회고: for 변수 in 리스트를 이용해서 원소 존재 여부를 확인하고 이중 for문이 아닌 하나의 for문으로 해결할 수 있었음
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, word in enumerate(words):
            for j in range(len(word)):
                if word[j] == x:
                    res.append(i)
                    break
        
        return res
        