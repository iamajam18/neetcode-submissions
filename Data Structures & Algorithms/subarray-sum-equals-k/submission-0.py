class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = {0:1}
        res = 0
        cur = 0
        for num in nums:
            cur += num
            diff = cur - k
            res += store.get(diff, 0)
            store[cur] = 1+ store.get(cur, 0)
        return res