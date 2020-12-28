class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for i,num in enumerate(nums):
	        if dic.get(num) != None and dic.get(num) != i:
                    return [dic[num],i]
	        dic[target-num] = i
        return []