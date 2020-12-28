class Solution:
    dic = dict()
    def fib(self, n: int) -> int:
        if self.dic.get(n) != None:
            return self.dic[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            res = self.fib(n-1) + self.fib(n-2)
            self.dic[n] = res
            return res
