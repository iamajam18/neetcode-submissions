class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shash = {}
        thash = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            shash[s[i]] = 1 + shash.get(s[i],0)
            thash[t[i]] = 1 + thash.get(t[i],0)
        return shash == thash
