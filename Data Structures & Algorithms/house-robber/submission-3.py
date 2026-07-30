class Solution:
    def rob(self, nums: List[int]) -> int:
        maxTwobefore, maxOnebefore = 0,0
        for n in nums:
            temp = max(n + maxTwobefore, maxOnebefore)
            maxTwobefore = maxOnebefore
            maxOnebefore = temp
        return maxOnebefore