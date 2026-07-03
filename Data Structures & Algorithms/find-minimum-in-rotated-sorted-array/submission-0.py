class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) -1
        while left<=right:
            if nums[left]<nums[right]:
                res = min(res,nums[left])
                break

            k = (left+right)//2
            res = min(res,nums[k])
            if nums[k]>=nums[left]:
                left = k+1
            else:
                right = k-1
        return res