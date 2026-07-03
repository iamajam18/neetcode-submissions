class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        for i in range(n):
            seen_chars = []
            for j in range(i,n):
                if s[j] not in seen_chars:
                    seen_chars.append(s[j])
                    longest = max(longest,len(seen_chars))
                else:
                    break
        return longest
