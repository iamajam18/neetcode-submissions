class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = {}
        res = 0
        l = 0
        maxf = 0

        for i in range(len(s)):
            store[s[i]] = 1 + store.get(s[i],0)
            maxf = max(maxf,store[s[i]])

            while (i-l+1) -maxf >k:
                store[s[l]] -= 1
                l +=1
            res = max(res,i-l+1)
        return res

