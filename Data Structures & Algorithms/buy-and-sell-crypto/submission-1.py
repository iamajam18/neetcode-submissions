class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        output = 0
        left, right = 0,1
        while right<n:
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                output = max(output,profit)
                right += 1
        return output