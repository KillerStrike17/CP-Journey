class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for _ in list(jewels):
            count+= stones.count(_)
        return count
        