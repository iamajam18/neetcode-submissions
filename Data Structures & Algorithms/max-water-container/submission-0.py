class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        left,right = 0,n-1
        while left<right:
            for i in range(n):
                if heights[left]<heights[right]:
                    length = heights[left]
                    current_area = length*(right-left)
                    left = left+1
                    max_area = max(max_area,current_area)
                else:
                    length = heights[right]
                    current_area = length*(right-left)
                    right = right-1
                    max_area = max(max_area,current_area)
        return max_area

