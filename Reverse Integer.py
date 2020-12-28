class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = x
        flag = 0
        if x < 0:
            flag = 1
            num = abs(num)    
        intMax = 2147483648
        rev = 0
        while num != 0:
            pop = num % 10
            num = num // 10
            if rev > (intMax//10) or (rev == intMax//10 and pop > 7):
                return 0
            rev = rev * 10 + pop
        return -rev if flag else rev