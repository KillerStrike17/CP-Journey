class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        else:
            sum_val = 0
            val_1 = 1
            val_2 = 2
            for _ in range(3, n+1):
                sum_val = val_1 + val_2
                val_1 = val_2
                val_2 = sum_val
            return sum_val
