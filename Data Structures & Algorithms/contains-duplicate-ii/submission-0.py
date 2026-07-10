class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = {}
        for i,num in enumerate(nums):
            if num in store and abs(store[num] - i) <=k:
                return True
            store[num] = i
        return False