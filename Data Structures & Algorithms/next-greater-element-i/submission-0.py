class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums1)
        store = {}
        for i, num in enumerate(nums1):
            store[num] = i
        for i in range(len(nums2)):
            if nums2[i] not in store:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idex = store[nums2[i]]
                    res[idex] = nums2[j]
                    break
        return res
            