class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0 , 1
        maxV = 0
        while r < len(prices):
            if prices[r]  >= prices[l]:
                maxV = max(prices[r] - prices[l], maxV)
            else:
                l = r
            r += 1
        return maxV

