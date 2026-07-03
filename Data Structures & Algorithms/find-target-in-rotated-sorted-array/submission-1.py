class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            k = (left+right)//2
            if nums[k] == target:
                return k
            if nums[left]<=nums[k]:
                if nums[left] <= target <nums[k]:
                    right = k-1
                else:
                    left = k+1
            else:
                if nums[k]<target<=nums[right]:
                    left=k+1
                else:
                    right = k-1
        return -1                