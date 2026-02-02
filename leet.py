class Solution:
    def __init__(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target

    def twoSum(self):
        for i in range(len(self.nums)):
            for j in range(i+1, len(self.nums)):
                if(self.nums[i]+self.nums[j] == self.target):
                    return [i,j]

        
t1 = Solution([1,2,3,4,5,6,7],5)
print(t1.twoSum())