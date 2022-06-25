class Solution:
    def maximumWealth(self, accounts) -> int:
        max_val = 0
        for _ in accounts:
            val = sum(_)
            if val > max_val:
                max_val = val
        return max_val
