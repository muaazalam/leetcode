class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left=0
        right=1
        maxP=0

        while right<len(prices):
            if prices[right]>prices[left]:
                curr=prices[right]-prices[left]
                maxP=max(maxP, curr)
            else:
                left=right
            right+=1

        return maxP

            

        