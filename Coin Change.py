from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dic = dict()
        
        def dp(n: int) -> int:
            # read
            if dic.get(n) != None:
                return dic.get(n)

            ret = float("inf")
            if n == 0: return 0
            if n < 0: return -1

            for coin in coins:
                r = dp(n - coin)

                if r == -1: continue
                ret = min(ret, r + 1)

            # write
            dic[n] = ret if ret != float("inf") else -1

            return dic.get(n)
        return dp(amount)